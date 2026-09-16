# Example Threat Model — Web API

This synthetic example contains no real production information.

## Assets

- user identity/token;
- profile data;
- privileged administrative action.

## Example threats

- stolen token used to impersonate a user;
- user modifies an object identifier to access another user's data;
- privileged action lacks immutable audit event;
- dependency compromise enters build pipeline.

## Example controls

- short-lived tokens and secure session handling;
- server-side object authorization on every request;
- append-only/audited privileged events;
- SCA, protected build identity, SBOM, signed immutable artifact.
