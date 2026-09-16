# Dockerfile Security

Prefer:

- minimal trusted base images;
- non-root runtime user;
- multi-stage builds;
- deterministic/pinned dependencies;
- no secrets in build layers;
- only required packages/files;
- read-only filesystem where the application allows it;
- current patched runtime/base image.
