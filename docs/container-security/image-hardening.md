# Image Hardening

- minimize base image and package count;
- use non-root users;
- remove compilers/debug tools when not needed at runtime;
- do not embed credentials;
- use read-only root filesystem where feasible;
- drop unnecessary Linux capabilities;
- set seccomp/AppArmor/SELinux controls where supported.
