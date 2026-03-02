# aerostack.StorageApi

All URIs are relative to *https://api.aerocall.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_upload**](StorageApi.md#storage_upload) | **POST** /storage/upload | Upload file to storage


# **storage_upload**
> StorageUpload200Response storage_upload(file, key, content_type=content_type)

Upload file to storage

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import aerostack
from aerostack.models.storage_upload200_response import StorageUpload200Response
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
    api_instance = aerostack.StorageApi(api_client)
    file = None # bytearray | 
    key = 'key_example' # str | Storage key/path
    content_type = 'content_type_example' # str |  (optional)

    try:
        # Upload file to storage
        api_response = api_instance.storage_upload(file, key, content_type=content_type)
        print("The response of StorageApi->storage_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **key** | **str**| Storage key/path | 
 **content_type** | **str**|  | [optional] 

### Return type

[**StorageUpload200Response**](StorageUpload200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File uploaded successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

