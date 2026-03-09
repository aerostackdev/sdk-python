# Aerostack Python SDK

[![PyPI version](https://img.shields.io/pypi/v/aerostack.svg)](https://pypi.org/project/aerostack/)
[![Python](https://img.shields.io/pypi/pyversions/aerostack.svg)](https://pypi.org/project/aerostack/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

The official Python SDK for the Aerostack Platform API. Unified access to database, authentication, caching, queues, storage, and AI services.

> **Note:** This SDK is auto-generated from the [OpenAPI specification](../../spec/openapi.yaml) using OpenAPI Generator. Do not hand-edit files in `aerostack/`.

## Features

- **Authentication** — User sign-up and sign-in
- **Database** — Execute SQL queries and batch operations
- **Cache** — Key-value caching with TTL, bulk operations, and atomic counters
- **Storage** — File upload, download, copy, move, delete, and metadata retrieval
- **Queue** — Background job scheduling, tracking, and cancellation
- **AI** — Chat completions, semantic search, vector ingestion, and configuration
- **Gateway** — Billing logs and wallet management
- **Services** — Cross-service invocation

## Requirements

Python 3.7+

## Installation

**pip (from Git)**

```bash
pip install git+https://github.com/aerostackdev/sdks.git#subdirectory=packages/python
```

**From source**

```bash
git clone https://github.com/aerostackdev/sdks.git
cd sdks/packages/python
pip install .
```

## Quick Start

```python
import os
import aerostack
from aerostack.rest import ApiException

# Configure the client
configuration = aerostack.Configuration(
    host="https://api.aerostack.dev/v1"
)
configuration.api_key['ApiKeyAuth'] = os.environ["AEROSTACK_API_KEY"]

with aerostack.ApiClient(configuration) as client:
    # Database query
    db = aerostack.DatabaseApi(client)
    result = db.db_query(aerostack.DbQueryRequest(
        sql="SELECT * FROM users LIMIT 10"
    ))
    print(f"Found {len(result.rows)} users")
```

## Usage Examples

### Authentication

```python
auth = aerostack.AuthenticationApi(client)

# Sign up
response = auth.auth_signup(aerostack.AuthSignupRequest(
    email="user@example.com",
    password="securePassword123"
))
print(f"User ID: {response.user.id}")

# Sign in
session = auth.auth_signin(aerostack.AuthSigninRequest(
    email="user@example.com",
    password="securePassword123"
))
```

### Cache Operations

```python
cache = aerostack.CacheApi(client)

# Set a value with TTL
cache.cache_set(aerostack.CacheSetRequest(
    key="session:user-123",
    value='{"name": "Alice"}',
    ttl=3600
))

# Get a value
result = cache.cache_get(aerostack.CacheGetRequest(key="session:user-123"))
print(f"Cached: {result.value}")

# Bulk operations
cache.cache_set_many(aerostack.CacheSetManyRequest(
    entries=[
        {"key": "k1", "value": "v1"},
        {"key": "k2", "value": "v2"},
    ]
))

# Atomic counter
cache.cache_increment(aerostack.CacheIncrementRequest(
    key="page-views",
    amount=1
))
```

### Storage

```python
storage = aerostack.StorageApi(client)

# Upload a file
with open("photo.jpg", "rb") as f:
    storage.storage_upload(file=f, key="photos/vacation.jpg")

# List objects
objects = storage.storage_list()
for obj in objects.objects:
    print(f"  {obj.key} ({obj.size} bytes)")

# Get metadata
meta = storage.storage_get_metadata(key="photos/vacation.jpg")
print(f"Content-Type: {meta.content_type}")
```

### Queue Jobs

```python
queue = aerostack.QueueApi(client)

# Enqueue a job
job = queue.queue_enqueue(aerostack.QueueEnqueueRequest(
    queue="email-notifications",
    payload={"to": "user@example.com", "template": "welcome"}
))
print(f"Job ID: {job.id}")

# Check job status
status = queue.queue_get_job(job_id=job.id)
print(f"Status: {status.status}")

# List jobs
jobs = queue.queue_list_jobs(queue="email-notifications")
```

### AI Chat & Search

```python
ai = aerostack.AIApi(client)

# Chat completion
response = ai.ai_chat(aerostack.AiChatRequest(
    messages=[
        aerostack.AiChatRequestMessagesInner(
            role="user",
            content="What is Aerostack?"
        )
    ]
))
print(response.choices[0].message.content)

# Ingest content for semantic search
ai.ingest(aerostack.IngestRequest(
    content="Aerostack is a full-stack cloud platform",
    type="documentation",
    id="doc-001"
))

# Search
results = ai.query(aerostack.QueryRequest(
    query="cloud platform features"
))
for r in results.results:
    print(f"  [{r.score:.2f}] {r.content[:80]}")
```

### Service Invocation

```python
services = aerostack.ServicesApi(client)

result = services.services_invoke(aerostack.ServicesInvokeRequest(
    service="payment-processor",
    method="charge",
    payload={"amount": 1999, "currency": "usd"}
))
```

## Error Handling

```python
from aerostack.rest import ApiException

try:
    auth.auth_signin(aerostack.AuthSigninRequest(
        email="user@example.com",
        password="wrong-password"
    ))
except ApiException as e:
    print(f"Status: {e.status}")
    print(f"Reason: {e.reason}")
    print(f"Body: {e.body}")
```

## API Reference

| Class | Key Methods |
|-------|-----------|
| `AuthenticationApi` | `auth_signin`, `auth_signup` |
| `DatabaseApi` | `db_query`, `db_batch` |
| `CacheApi` | `cache_get`, `cache_set`, `cache_delete`, `cache_list`, `cache_keys`, `cache_get_many`, `cache_set_many`, `cache_delete_many`, `cache_flush`, `cache_expire`, `cache_increment` |
| `StorageApi` | `storage_upload`, `storage_get`, `storage_list`, `storage_delete`, `storage_exists`, `storage_get_metadata`, `storage_move`, `storage_copy` |
| `QueueApi` | `queue_enqueue`, `queue_get_job`, `queue_list_jobs`, `queue_cancel_job` |
| `AIApi` | `ai_chat`, `ingest`, `query`, `delete`, `delete_by_type`, `list_types`, `configure` |
| `GatewayApi` | `gateway_billing_log`, `gateway_get_wallet` |
| `ServicesApi` | `services_invoke` |

## Documentation for API Endpoints

All URIs are relative to `https://api.aerostack.dev/v1`

| Class | Method | HTTP Request | Description |
|-------|--------|-------------|-------------|
| `AIApi` | `ai_chat` | **POST** /ai/chat | Generate AI chat completion |
| `AIApi` | `configure` | **POST** /ai/search/configure | Update search configuration |
| `AIApi` | `delete` | **POST** /ai/search/delete | Delete item by ID |
| `AIApi` | `delete_by_type` | **POST** /ai/search/deleteByType | Delete all items of a type |
| `AIApi` | `ingest` | **POST** /ai/search/ingest | Ingest content into search index |
| `AIApi` | `list_types` | **GET** /ai/search/listTypes | List distinct types and counts |
| `AIApi` | `query` | **POST** /ai/search/query | Search managed index |
| `AuthenticationApi` | `auth_signin` | **POST** /auth/signin | Sign in user |
| `AuthenticationApi` | `auth_signup` | **POST** /auth/signup | Sign up new user |
| `CacheApi` | `cache_get` | **POST** /cache/get | Get cached value |
| `CacheApi` | `cache_set` | **POST** /cache/set | Set cached value |
| `DatabaseApi` | `db_query` | **POST** /db/query | Execute SQL query |
| `GatewayApi` | `gateway_billing_log` | **POST** /gateway/billing/log | Log Gateway usage |
| `QueueApi` | `queue_enqueue` | **POST** /queue/enqueue | Add job to queue |
| `ServicesApi` | `services_invoke` | **POST** /services/invoke | Invoke another service |
| `StorageApi` | `storage_upload` | **POST** /storage/upload | Upload file to storage |

## Documentation for Models

- [AiChat200Response](docs/AiChat200Response.md)
- [AiChatRequest](docs/AiChatRequest.md)
- [AiChatRequestMessagesInner](docs/AiChatRequestMessagesInner.md)
- [AuthResponse](docs/AuthResponse.md)
- [AuthSigninRequest](docs/AuthSigninRequest.md)
- [AuthSignupRequest](docs/AuthSignupRequest.md)
- [CacheGet200Response](docs/CacheGet200Response.md)
- [CacheGetRequest](docs/CacheGetRequest.md)
- [CacheSet200Response](docs/CacheSet200Response.md)
- [CacheSetRequest](docs/CacheSetRequest.md)
- [ConfigureRequest](docs/ConfigureRequest.md)
- [DbQueryRequest](docs/DbQueryRequest.md)
- [DbQueryResult](docs/DbQueryResult.md)
- [DeleteByTypeRequest](docs/DeleteByTypeRequest.md)
- [DeleteRequest](docs/DeleteRequest.md)
- [ErrorResponse](docs/ErrorResponse.md)
- [GatewayBillingLog200Response](docs/GatewayBillingLog200Response.md)
- [GatewayBillingLogRequest](docs/GatewayBillingLogRequest.md)
- [IngestRequest](docs/IngestRequest.md)
- [ListTypes200Response](docs/ListTypes200Response.md)
- [Query200Response](docs/Query200Response.md)
- [QueryRequest](docs/QueryRequest.md)
- [QueueEnqueue201Response](docs/QueueEnqueue201Response.md)
- [QueueEnqueueRequest](docs/QueueEnqueueRequest.md)
- [SearchResult](docs/SearchResult.md)
- [ServicesInvoke200Response](docs/ServicesInvoke200Response.md)
- [ServicesInvokeRequest](docs/ServicesInvokeRequest.md)
- [StorageUpload200Response](docs/StorageUpload200Response.md)
- [TypeStats](docs/TypeStats.md)
- [User](docs/User.md)

## Authorization

All API calls require an API key passed via the `X-Aerostack-Key` header:

```python
configuration = aerostack.Configuration()
configuration.api_key['ApiKeyAuth'] = 'your-api-key'
```

## Running Tests

```bash
pytest
```

## Related SDKs

| SDK | Language | Use Case |
|-----|----------|----------|
| [`@aerostack/node`](../node) | TypeScript | Node.js server |
| [`@aerostack/web`](../web) | TypeScript | Browser apps |
| [`@aerostack/react`](../react) | TypeScript | React apps |
| [`@aerostack/flutter`](../flutter) | Dart | Flutter mobile |
| [`aerostack` CLI](../cli) | Go | Project management |

## Documentation

For full documentation, visit [docs.aerostack.dev](https://docs.aerostack.dev/sdk/python).

## License

MIT
