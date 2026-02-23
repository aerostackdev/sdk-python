# Gateway.Billing

## Overview

### Available Operations

* [gateway_billing_log](#gateway_billing_log) - Log Gateway usage

## gateway_billing_log

Manually log tokens or custom metric usage for a Gateway API

### Example Usage

<!-- UsageSnippet language="python" operationID="gatewayBillingLog" method="post" path="/gateway/billing/log" -->
```python
from aerostack import SDK


with SDK(
    api_key_auth="<YOUR_API_KEY_HERE>",
) as sdk:

    res = sdk.gateway.billing.gateway_billing_log(request={
        "consumer_id": "usr_123xyz",
        "api_id": "api_chat_bot",
        "metric": "tokens",
        "units": 1500,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.GatewayBillingLogRequestBody](../../models/gatewaybillinglogrequestbody.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.GatewayBillingLogResponseBody](../../models/gatewaybillinglogresponsebody.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400, 401             | application/json     |
| errors.SDKError      | 4XX, 5XX             | \*/\*                |