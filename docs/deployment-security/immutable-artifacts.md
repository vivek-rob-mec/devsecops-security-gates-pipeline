# Immutable Artifact Promotion

Preferred model:

```text
Build once → app@sha256:ABC → Dev → QA → Staging → Production
```

Avoid rebuilding source separately for each environment. Environment configuration should be injected independently from the immutable application artifact.
