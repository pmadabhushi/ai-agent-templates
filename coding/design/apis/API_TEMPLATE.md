# API: [APIName / ServiceName API]

## Overview

[One-paragraph description of the API surface, who consumes it, and its role.]

## Base URL

- **Dev:** `[https://dev.example.com/api/v1]`
- **Staging:** `[https://staging.example.com/api/v1]`
- **Prod:** `[https://api.example.com/api/v1]`

## Authentication

- **Method:** [e.g., IAM SigV4, OAuth 2.0 Bearer, API Key]
- **Required headers:** [e.g., `Authorization: Bearer <token>`]

## Endpoints

### [POST /resource]

**Description:** [What this endpoint does]

**Request:**
```json
{
  "[field]": "[type — description]",
  "[field]": "[type — description]"
}
```

**Response (200):**
```json
{
  "[field]": "[type — description]",
  "[field]": "[type — description]"
}
```

**Errors:**

| Status | Code | Description |
|---|---|---|
| 400 | [ErrorCode] | [When this happens] |
| 403 | [ErrorCode] | [When this happens] |
| 500 | [ErrorCode] | [When this happens] |

### [GET /resource/:id]

**Description:** [What this endpoint does]

**Path params:** `id` — [description]

**Response (200):**
```json
{
  "[field]": "[type — description]"
}
```

## Rate Limits

| Tier | Limit | Scope |
|---|---|---|
| [Default] | [X requests/sec] | [Per account / per API key] |
| [Elevated] | [Y requests/sec] | [Per account — requires approval] |

## Pagination

- **Strategy:** [e.g., cursor-based, offset-based]
- **Default page size:** [X]
- **Max page size:** [Y]

## Versioning

- **Strategy:** [e.g., URL path /v1/, header-based]
- **Current version:** [v1]
- **Deprecation policy:** [e.g., 6-month notice before removal]

## Contract Tests

- **Location:** [path to contract tests in repo]
- **How to run:** `[test command]`

## Related Docs

- OpenAPI spec: [Link]
- Design doc: [Link]
- SDK documentation: [Link]
