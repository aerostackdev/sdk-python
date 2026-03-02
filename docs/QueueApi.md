# aerostack.QueueApi

All URIs are relative to *https://api.aerocall.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queue_enqueue**](QueueApi.md#queue_enqueue) | **POST** /queue/enqueue | Add job to queue


# **queue_enqueue**
> QueueEnqueue201Response queue_enqueue(queue_enqueue_request)

Add job to queue

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import aerostack
from aerostack.models.queue_enqueue201_response import QueueEnqueue201Response
from aerostack.models.queue_enqueue_request import QueueEnqueueRequest
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
    api_instance = aerostack.QueueApi(api_client)
    queue_enqueue_request = aerostack.QueueEnqueueRequest() # QueueEnqueueRequest | 

    try:
        # Add job to queue
        api_response = api_instance.queue_enqueue(queue_enqueue_request)
        print("The response of QueueApi->queue_enqueue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueueApi->queue_enqueue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_enqueue_request** | [**QueueEnqueueRequest**](QueueEnqueueRequest.md)|  | 

### Return type

[**QueueEnqueue201Response**](QueueEnqueue201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Job enqueued successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

