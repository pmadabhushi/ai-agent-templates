# Architecture: [ServiceName / ComponentName]

## Overview

[One-paragraph description of the component's purpose and role in the system.]

## Ownership

- **Team:** [TeamName]
- **Primary language:** [Language]
- **Repo:** [repo link]

## Component Structure

```
[component-name]/
├── [package-1]/    # [purpose]
├── [package-2]/    # [purpose]
├── [package-3]/    # [purpose]
└── [tests]/        # [test types]
```

## Key Classes / Modules

| Class / Module | Responsibility |
|---|---|
| [ClassName] | [What it does, e.g., "Handles request validation and routing"] |
| [ClassName] | [What it does] |
| [ClassName] | [What it does] |

## Dependencies

| Dependency | Type | Purpose |
|---|---|---|
| [Library / Service] | [Internal / External] | [Why it's used] |
| [Library / Service] | [Internal / External] | [Why it's used] |

## Data Model

| Entity | Storage | Key Fields |
|---|---|---|
| [EntityName] | [e.g., DynamoDB, RDS, in-memory] | [key fields] |
| [EntityName] | [e.g., S3, Redis] | [key fields] |

## API Contracts

| Endpoint / Method | Input | Output | Notes |
|---|---|---|---|
| [POST /api/resource] | [RequestDTO] | [ResponseDTO] | [e.g., Requires auth] |
| [GET /api/resource/:id] | [path param] | [ResponseDTO] | [e.g., Cached 60s] |

## Design Decisions

| Decision | Rationale | Date |
|---|---|---|
| [e.g., Chose event-driven over sync] | [e.g., Decouples producers from consumers] | [date] |
| [e.g., DynamoDB single-table design] | [e.g., Reduces latency, simplifies queries] | [date] |

## Related Docs

- Design doc: [Link]
- API spec: [Link]
- ADR / RFC: [Link]
