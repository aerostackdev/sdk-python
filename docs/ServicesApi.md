# aerostack.ServicesApi

All URIs are relative to *https://api.aerocall.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**services_invoke**](ServicesApi.md#services_invoke) | **POST** /services/invoke | Invoke another service


# **services_invoke**
> ServicesInvoke200Response services_invoke(services_invoke_request)

Invoke another service

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import aerostack
from aerostack.models.services_invoke200_response import ServicesInvoke200Response
from aerostack.models.services_invoke_request import ServicesInvokeRequest
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
    api_instance = aerostack.ServicesApi(api_client)
    services_invoke_request = aerostack.ServicesInvokeRequest() # ServicesInvokeRequest | 

    try:
        # Invoke another service
        api_response = api_instance.services_invoke(services_invoke_request)
        print("The response of ServicesApi->services_invoke:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->services_invoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **services_invoke_request** | [**ServicesInvokeRequest**](ServicesInvokeRequest.md)|  | 

### Return type

[**ServicesInvoke200Response**](ServicesInvoke200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service invoked successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

