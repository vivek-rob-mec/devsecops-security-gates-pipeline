# API Security Testing

Useful inputs:

- OpenAPI specification;
- GraphQL schema;
- authenticated test identities with multiple roles;
- negative authorization cases;
- rate-limit and abuse scenarios;
- invalid/malformed payloads;
- sensitive-data assertions.

<!-- course-explanation -->
## Working principle and implementation status

**TEST IDENTITY.** Create customer A, customer B and an administrative role using isolated test accounts.

**TEST OWNERSHIP.** Request A’s order as B. Expect access denial and no order data, including through alternate routes.

**TEST BOUNDARIES.** Check role changes, pagination, bulk endpoints, expired sessions and rate-sensitive operations.

Authentication answers who the requester is. Authorization answers whether that requester may perform this action on this object. Broken Object Level Authorization, or BOLA, and Insecure Direct Object Reference, or IDOR, describe related object-access failures. A generic scanner usually cannot infer the intended customer ownership model. API schema testing can find malformed input handling, while deliberate role and ownership tests establish business rules. Save expected and observed results, but redact tokens and customer information. Run these tests against the same candidate digest used for other staging checks.

Read the [complete lesson and primary sources](../DEVSECOPS_HANDBOOK.md#lesson-28), [data/update matrix](../DETECTION_AND_DATA.md) and [implementation quickstart](../implementation/quickstart.md).
<!-- /course-explanation -->
