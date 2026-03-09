# aerostack.CacheApi

All URIs are relative to *https://api.aerostack.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cache_get**](CacheApi.md#cache_get) | **POST** /cache/get | Get cached value
[**cache_set**](CacheApi.md#cache_set) | **POST** /cache/set | Set cached value


# **cache_get**
> CacheGet200Response cache_get(cache_get_request)

Get cached value

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import aerostack
from aerostack.models.cache_get200_response import CacheGet200Response
from aerostack.models.cache_get_request import CacheGetRequest
from aerostack.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.aerostack.dev/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aerostack.Configuration(
    host = "https://api.aerostack.dev/v1"
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
    api_instance = aerostack.CacheApi(api_client)
    cache_get_request = aerostack.CacheGetRequest() # CacheGetRequest | 

    try:
        # Get cached value
        api_response = api_instance.cache_get(cache_get_request)
        print("The response of CacheApi->cache_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CacheApi->cache_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cache_get_request** | [**CacheGetRequest**](CacheGetRequest.md)|  | 

### Return type

[**CacheGet200Response**](CacheGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cache value retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cache_set**
> CacheSet200Response cache_set(cache_set_request)

Set cached value

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import aerostack
from aerostack.models.cache_set200_response import CacheSet200Response
from aerostack.models.cache_set_request import CacheSetRequest
from aerostack.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.aerostack.dev/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aerostack.Configuration(
    host = "https://api.aerostack.dev/v1"
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
    api_instance = aerostack.CacheApi(api_client)
    cache_set_request = aerostack.CacheSetRequest() # CacheSetRequest | 

    try:
        # Set cached value
        api_response = api_instance.cache_set(cache_set_request)
        print("The response of CacheApi->cache_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CacheApi->cache_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cache_set_request** | [**CacheSetRequest**](CacheSetRequest.md)|  | 

### Return type

[**CacheSet200Response**](CacheSet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Value cached successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

