"""Offline regression tests for wrapper contracts, using fake scanner commands."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
GIT_BASH = Path('C:/Program Files/Git/bin/bash.exe')
BASH = str(GIT_BASH) if GIT_BASH.exists() else shutil.which('bash')

def shell_path(path):
    value=Path(path).resolve().as_posix()
    if os.name=='nt' and len(value)>2 and value[1]==':':
        return '/'+value[0].lower()+value[2:]
    return value

FAKE = '''#!/usr/bin/env bash
name="${0##*/}"
printf '%s\\n' "$name" "$@" >> "$CALL_LOG"
if [[ "$name" == git ]]; then
  exit "${FAKE_GIT_STATUS:-1}"
fi
exit "${FAKE_EXIT:-0}"
'''

@unittest.skipUnless(BASH, 'Bash is required to validate Bash wrappers')
class WrapperTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='wrapper-tests-')
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.bin = self.folder/'fake-bin'
        self.bin.mkdir()
        self.log = self.folder/'calls.txt'
        for name in ('trivy','gitleaks','semgrep','cosign','syft','git'):
            f=self.bin/name
            f.write_text(FAKE,encoding='utf-8',newline='\n')
            f.chmod(0o755)

    def run_wrapper(self, name, **settings):
        env=dict(os.environ)
        for key in ('IMAGE_REF','SEMGREP_CONFIG','DAST_TARGET_URL','REPORT_DIR'):
            env.pop(key,None)
        # Export PATH in Bash so Windows drive-letter colons are converted correctly.
        env.update(FAKE_BIN=shell_path(self.bin), CALL_LOG=shell_path(self.log),
                   REPORT_DIR=shell_path(self.folder/'reports'))
        env.update(settings)
        result=subprocess.run([BASH,'-c','export PATH="$FAKE_BIN:$PATH"; exec bash "$1"',
                               'wrapper-test',(ROOT/'scripts'/name).as_posix()],
                              cwd=self.folder,env=env,capture_output=True,text=True,timeout=20)
        calls=self.log.read_text(encoding='utf-8').splitlines() if self.log.exists() else []
        return result,calls

    def test_trivy_findings_and_errors_propagate(self):
        for name in ('sca-scan.sh','iac-scan.sh','image-scan.sh'):
            for code in ('1','7'):
                with self.subTest(wrapper=name,status=code):
                    result,calls=self.run_wrapper(name,FAKE_EXIT=code,
                        IMAGE_REF='registry.example/shop@sha256:'+'a'*64)
                    self.assertEqual(result.returncode,int(code),result.stderr)
                    self.assertIn('--exit-code',calls)
                    self.assertIn('--config',calls)
                    self.assertTrue(any(x.endswith('configs/trivy/trivy.yaml') for x in calls))

    def test_trivy_passes_success(self):
        result,calls=self.run_wrapper('sca-scan.sh')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertIn('vuln',calls)

    def test_semgrep_explicit_rules_and_failure(self):
        result,calls=self.run_wrapper('sast-scan.sh',FAKE_EXIT='1')
        self.assertEqual(result.returncode,1,result.stderr)
        self.assertIn('--error',calls)
        self.assertIn('--strict',calls)
        self.assertNotIn('auto',calls)
        self.assertTrue(any(x.endswith('configs/semgrep/semgrep.yml') for x in calls))

    def test_semgrep_custom_rules(self):
        result,calls=self.run_wrapper('sast-scan.sh',SEMGREP_CONFIG='reviewed-rules')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertIn('reviewed-rules',calls)

    def test_worktree_scan_without_git_history(self):
        result,calls=self.run_wrapper('secret-scan.sh',FAKE_GIT_STATUS='1')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertIn('dir',calls)
        self.assertEqual(calls.count('gitleaks'),1)
        self.assertIn('--redact',calls)

    def test_history_scan_when_git_metadata_exists(self):
        result,calls=self.run_wrapper('secret-scan.sh',FAKE_GIT_STATUS='0')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(calls.count('gitleaks'),2)
        self.assertIn('--log-opts=--all',calls)

    def test_secret_finding_blocks(self):
        result,_=self.run_wrapper('secret-scan.sh',FAKE_EXIT='1')
        self.assertEqual(result.returncode,1,result.stderr)

    def test_image_mutable_or_malformed_reference_rejected(self):
        for name in ('image-scan.sh','generate-sbom.sh','sign-artifact.sh'):
            for ref in ('','shop:latest','shop@sha256:abc','shop@sha256:'+'A'*64):
                with self.subTest(wrapper=name,reference=ref):
                    result,calls=self.run_wrapper(name,IMAGE_REF=ref)
                    self.assertEqual(result.returncode,2,result.stderr)
                    self.assertFalse(calls)

    def test_immutable_digest_is_passed_unchanged(self):
        ref='registry.example:5000/team/shop@sha256:'+'b'*64
        for name in ('image-scan.sh','generate-sbom.sh','sign-artifact.sh'):
            with self.subTest(wrapper=name):
                result,calls=self.run_wrapper(name,IMAGE_REF=ref)
                self.assertEqual(result.returncode,0,result.stderr)
                self.assertIn(ref,calls)

    def test_sbom_and_signing_failure_propagate(self):
        for name in ('generate-sbom.sh','sign-artifact.sh'):
            with self.subTest(wrapper=name):
                result,_=self.run_wrapper(name,IMAGE_REF='shop@sha256:'+'a'*64,FAKE_EXIT='9')
                self.assertEqual(result.returncode,9,result.stderr)

    def test_unimplemented_gates_cannot_pass(self):
        for name in ('dast-scan.sh','security-gate.sh'):
            with self.subTest(wrapper=name):
                result,_=self.run_wrapper(name,DAST_TARGET_URL='https://staging.example.invalid')
                self.assertEqual(result.returncode,2,result.stderr)

    def test_missing_command_fails(self):
        result=subprocess.run([BASH,'-c','source "$1"; require_cmd nonexistent_security_tool_for_test',
                               'missing-command',(ROOT/'scripts/lib/common.sh').as_posix()],
                              env={**os.environ,'REPORT_DIR':(self.folder/'reports').as_posix()},
                              capture_output=True,text=True,timeout=20)
        self.assertEqual(result.returncode,127,result.stderr)

if __name__=='__main__': unittest.main()
