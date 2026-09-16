# Secret Scanning

Secret scanning detects credentials and sensitive tokens before they become deployable artifacts.

Recommended layers:

- developer/pre-commit (optional fast feedback);
- PR/current-tree scanning;
- CI scan;
- server-side repository secret scanning;
- periodic full-history scan for legacy exposure.

A current-tree scan is fast but cannot tell you whether a secret existed in an older commit. Choose scope deliberately.

If a real credential is committed, **removing the file is not enough**. Revoke/rotate the credential and assess exposure; rewriting Git history is a separate cleanup action.
