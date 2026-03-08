# Security Control: [ControlName]

## Overview

[One-paragraph description of the control, what risk it mitigates, and how it works.]

## Control Details

- **Control type:** [Preventive / Detective / Corrective]
- **Implementation:** [Automated / Manual / Hybrid]
- **Risk mitigated:** [e.g., Unauthorized access, Data exfiltration, Secret exposure]
- **Compliance mapping:** [e.g., SOC2 CC6.1, PCI-DSS Req 7.1]

## Architecture

```
[How the control fits into the system]

[Request] → [Control Point: e.g., WAF / IAM / Scanner]
                        ↓ (allow/deny)
                  [Protected Resource]
                        ↓
                  [Audit Log]
```

## Configuration

| Parameter | Value | Description |
|---|---|---|
| [e.g., Rate limit] | [e.g., 1000 req/s] | [What it controls] |
| [e.g., Block threshold] | [e.g., 5 failed attempts] | [What it controls] |
| [e.g., Scan frequency] | [e.g., Every commit] | [What it controls] |

## Monitoring & Alerting

| Metric | Normal | Alert Threshold | Action |
|---|---|---|---|
| [e.g., Blocked requests] | [< X/min] | [> Y/min] | [Investigate, check for attack] |
| [e.g., Failed auth attempts] | [< X/hr] | [> Y/hr] | [Lock account, alert security] |

## Testing

- **How to verify the control works:** [e.g., Run penetration test, trigger test alert]
- **Test frequency:** [e.g., Monthly, per release, annually]
- **Last tested:** [date]
- **Test evidence:** [link]

## Failure Mode

| Failure Scenario | Behavior | Impact | Recovery |
|---|---|---|---|
| [e.g., Control service down] | [e.g., Fail-open / Fail-closed] | [e.g., Requests bypass check] | [e.g., Auto-restart, alert on-call] |

## Related Docs

- Threat model: [Link]
- Policy: [Link]
- Audit evidence: [Link]
