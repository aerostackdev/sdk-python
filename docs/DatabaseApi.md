# aerostack.DatabaseApi

All URIs are relative to *https://api.aerocall.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**db_query**](DatabaseApi.md#db_query) | **POST** /db/query | Execute SQL query


# **db_query**
> DbQueryResult db_query(db_query_request, x_request_id=x_request_id, x_sdk_version=x_sdk_version)

Execute SQL query

Run a SQL query against your project database

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import aerostack
from aerostack.models.db_query_request import DbQueryRequest
from aerostack.models.db_query_result import DbQueryResult
from aerostack.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.aerocall.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aerostack.Configuration(
    host = "https://api.aerocall.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with aerostack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aerostack.DatabaseApi(api_client)
    db_query_request = aerostack.DbQueryRequest() # DbQueryRequest | 
    x_request_id = 'x_request_id_example' # str | Unique request tracing ID (optional)
    x_sdk_version = '0.1.0' # str | SDK version string (optional)

    try:
        # Execute SQL query
        api_response = api_instance.db_query(db_query_request, x_request_id=x_request_id, x_sdk_version=x_sdk_version)
        print("The response of DatabaseApi->db_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->db_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_query_request** | [**DbQueryRequest**](DbQueryRequest.md)|  | 
 **x_request_id** | **str**| Unique request tracing ID | [optional] 
 **x_sdk_version** | **str**| SDK version string | [optional] 

### Return type

[**DbQueryResult**](DbQueryResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query executed successfully |  -  |
**400** |  |  -  |
**401** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

