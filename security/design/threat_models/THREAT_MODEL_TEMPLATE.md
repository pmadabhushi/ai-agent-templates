# Threat Model: [ServiceName / FeatureName]

## Overview

[One-paragraph description of what is being threat-modeled and its security context.]

## Scope

- **Service(s):** [list services in scope]
- **Data classification:** [Confidential / Internal / Public]
- **Compliance frameworks:** [SOC2, PCI-DSS, HIPAA, etc.]
- **Last reviewed:** [date]
- **Next review due:** [date]

## Assets

| Asset | Classification | Storage | Access |
|---|---|---|---|
| [e.g., Customer PII] | [Confidential] | [e.g., RDS encrypted] | [e.g., Service role only] |
| [e.g., API keys] | [Secret] | [e.g., Secrets Manager] | [e.g., Rotation every 90d] |
| [e.g., Audit logs] | [Internal] | [e.g., S3 with lifecycle] | [e.g., Security team read-only] |

## Trust Boundaries

```
[External Users] ──TLS──→ [API Gateway / CDN]
                                  ↓
                           [Auth Layer] ──IAM──→ [Service]
                                                     ↓
                                              [Datastore] (encrypted at rest)
```

## Threat Analysis (STRIDE)

| Category | Threat | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| **Spoofing** | [e.g., Forged auth tokens] | [H/M/L] | [H/M/L] | [e.g., Token validation, short TTL] |
| **Tampering** | [e.g., Modified request payload] | [H/M/L] | [H/M/L] | [e.g., Input validation, request signing] |
| **Repudiation** | [e.g., Denied actions without audit trail] | [H/M/L] | [H/M/L] | [e.g., Immutable audit logs] |
| **Info Disclosure** | [e.g., Verbose error messages leak internals] | [H/M/L] | [H/M/L] | [e.g., Generic error responses, structured logging] |
| **Denial of Service** | [e.g., Unthrottled API endpoint] | [H/M/L] | [H/M/L] | [e.g., Rate limiting, WAF rules] |
| **Elevation of Privilege** | [e.g., IDOR on resource access] | [H/M/L] | [H/M/L] | [e.g., Resource-level authz checks] |

## Open Risks

| Risk | Severity | Owner | Status | Ticket |
|---|---|---|---|---|
| [Description] | [Critical/High/Medium/Low] | [team/person] | [Open/Mitigated/Accepted] | [link] |

## Related Docs

- Architecture doc: [Link]
- Compliance evidence: [Link]
- Previous threat model: [Link]
