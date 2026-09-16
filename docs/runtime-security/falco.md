# Falco

Falco can detect suspicious Linux/container runtime behavior using rules. Treat alerts as detection signals that need tuning, context, routing, and incident-response ownership.

<!-- course-explanation -->
## Working principle and implementation status

**OBSERVE.** System activity and supported event sources produce process, file and other runtime context.

**MATCH.** Rules compare event fields and conditions with behaviors worth investigating.

**RESPOND.** Route alerts to an owner. Investigate, contain when justified, preserve evidence and correct the cause.

Falco rules define event conditions and alert messages. Depending on deployment, a driver or plugin supplies the events. This is behavior detection, not an inventory-to-CVE comparison. Rules, exceptions and engine support need maintenance. Starting a shell inside an application container may be suspicious but can also be an authorized operational action, so context matters. SIEM means Security Information and Event Management, a system for collecting and correlating events. EDR means Endpoint Detection and Response. The repository documents these controls but does not install a runtime sensor or automate incident response.

Read the [complete lesson and primary sources](../DEVSECOPS_HANDBOOK.md#lesson-30), [data/update matrix](../DETECTION_AND_DATA.md) and [implementation quickstart](../implementation/quickstart.md).
<!-- /course-explanation -->
