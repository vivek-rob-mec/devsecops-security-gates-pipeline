# Kubernetes Manifest Security

Review for:

- privileged containers;
- hostPath/hostNetwork/hostPID use;
- root execution;
- missing seccomp/profile restrictions;
- overly broad RBAC;
- plaintext Secret manifests in Git;
- unpinned images;
- missing resource boundaries;
- unrestricted ingress/egress where policy requires segmentation.
