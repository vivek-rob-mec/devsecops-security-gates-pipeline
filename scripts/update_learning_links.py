"""Keep short topic pages connected to the complete offline course."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'presentation'))
from course_content import SLIDES

TOPICS={
 'docs/secret-scanning/gitleaks.md':'Secret scanning: Gitleaks',
 'docs/sca/trivy.md':'Trivy: source and image vulnerabilities',
 'docs/sca/dependency-check.md':'Dependency-Check, OSV and Grype',
 'docs/sast/semgrep.md':'Semgrep: executable rules over code',
 'docs/sast/codeql.md':'CodeQL and SonarQube use different models',
 'docs/sast/sonarqube.md':'CodeQL and SonarQube use different models',
 'docs/iac-security/checkov-trivy.md':'IaC scanning: compare desired state to policy',
 'docs/container-security/image-scanning.md':'Containers: inspect what actually ships',
 'docs/sbom/sbom-generation.md':'SBOM: inventory for today and tomorrow',
 'docs/supply-chain/cosign.md':'Signing and provenance establish origin',
 'docs/dast/zap.md':'ZAP: baseline is not a full active test',
 'docs/api-security/api-security-testing.md':'API security needs business-aware assertions',
 'docs/runtime-security/falco.md':'Runtime detection: notice suspicious behavior',
}

def main():
    import re
    for path,title in TOPICS.items():
        index=next(i for i,s in enumerate(SLIDES,1) if s['title']==title)
        item=SLIDES[index-1]
        target=ROOT/path
        existing=target.read_text(encoding='utf-8')
        existing=re.sub(r'\n<!-- course-explanation -->.*?<!-- /course-explanation -->\n','\n',existing,flags=re.S)
        detail='\n<!-- course-explanation -->\n## Working principle and implementation status\n\n'
        for heading,body in item['cards']:
            detail+='**'+heading+'.** '+body.replace('\n','; ')+'\n\n'
        detail+=item['notes']+'\n\n'
        detail+=f'Read the [complete lesson and primary sources](../DEVSECOPS_HANDBOOK.md#lesson-{index:02d}), [data/update matrix](../DETECTION_AND_DATA.md) and [implementation quickstart](../implementation/quickstart.md).\n<!-- /course-explanation -->\n'
        target.write_text(existing.rstrip()+'\n'+detail,encoding='utf-8')
    print(f'Updated {len(TOPICS)} topic pages with explanations and course links.')

if __name__=='__main__': main()
