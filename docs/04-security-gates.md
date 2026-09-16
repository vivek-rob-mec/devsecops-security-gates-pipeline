# Security Gates

## Scanner vs gate

A scanner produces findings. A gate evaluates findings and contextual policy to decide whether progression is allowed.

A robust gate considers:

- severity;
- exploitability/reachability;
- affected environment;
- internet exposure;
- fix availability;
- asset/data criticality;
- finding age;
- whether the finding is new or pre-existing;
- approved exception status;
- compensating controls.

## Gate types

- **Hard gate** — pipeline stops until remediation or approved exception.
- **Soft gate** — pipeline continues but produces visible debt/notification.
- **Manual approval gate** — required for defined risks or sensitive production changes.
- **Observation-only** — useful while introducing a new scanner to measure noise before enforcement.

Do not blindly fail on every finding on day one. Establish signal quality, ownership, baselines, and an adoption path.
