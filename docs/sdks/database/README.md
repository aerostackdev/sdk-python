# Database

## Overview

SQL database operations

### Available Operations

* [db_query](#db_query) - Execute SQL query

## db_query

Run a SQL query against your project database

### Example Usage

<!-- UsageSnippet language="python" operationID="dbQuery" method="post" path="/db/query" -->
```python
from aerostack import SDK


with SDK(
    api_key_auth="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.database.db_query(request_body={
        "sql": "SELECT * FROM users WHERE active = ?",
        "params": [
            True,
        ],
    }, x_sdk_version="0.1.0")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request_body`                                                      | [models.DbQueryRequestBody](../../models/dbqueryrequestbody.md)     | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `x_request_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Unique request tracing ID                                           |                                                                     |
| `x_sdk_version`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | SDK version string                                                  | 0.1.0                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DbQueryResult](../../models/dbqueryresult.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400, 401             | application/json     |
| errors.ErrorResponse | 500                  | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |