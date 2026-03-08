# Pattern: [PatternName]

## Overview

[One-paragraph description of the pattern, when to use it, and what problem it solves.]

## When to Use

- [Scenario 1, e.g., "When integrating a new external service"]
- [Scenario 2, e.g., "When adding a new API endpoint that requires validation"]
- [Scenario 3, e.g., "When implementing async processing with retries"]

## When NOT to Use

- [Anti-scenario 1, e.g., "Simple CRUD with no business logic"]
- [Anti-scenario 2, e.g., "Internal-only utilities with no external dependencies"]

## Structure

```
[Diagram or pseudocode showing the pattern structure]

[Caller] → [Interface / Contract]
                  ↓
           [Implementation]
                  ↓
           [Dependency / Adapter]
```

## Implementation Template

```[language]
// [Annotated code template showing the pattern]
// Replace placeholders with your specific implementation

[code template]
```

## Error Handling

| Error Type | Handling Strategy |
|---|---|
| [e.g., Validation error] | [e.g., Return 400 with field-level errors] |
| [e.g., Dependency timeout] | [e.g., Retry 3x with backoff, then circuit break] |
| [e.g., Unexpected exception] | [e.g., Log, wrap in ServiceException, return 500] |

## Testing Strategy

- **Unit tests:** [What to mock, what to assert]
- **Integration tests:** [What to test end-to-end]
- **Contract tests:** [Required for public APIs — verify request/response schemas]

## Examples in Codebase

| Location | Description |
|---|---|
| [path/to/file] | [How this pattern is used there] |
| [path/to/file] | [How this pattern is used there] |

## Related Patterns

- [RelatedPattern1] — [how it relates]
- [RelatedPattern2] — [how it relates]
