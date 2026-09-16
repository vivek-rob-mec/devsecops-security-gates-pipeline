# Security-Aware Code Review

Reviewers should look beyond style and correctness for:

- trust-boundary changes;
- authorization decisions;
- unsafe deserialization or command execution;
- injection paths;
- cryptographic misuse;
- sensitive logging;
- new secrets;
- dependency additions;
- unsafe file/network handling;
- privilege changes.
