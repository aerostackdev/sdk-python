# aerostack.AuthenticationApi

All URIs are relative to *https://api.aerocall.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_signin**](AuthenticationApi.md#auth_signin) | **POST** /auth/signin | Sign in user
[**auth_signup**](AuthenticationApi.md#auth_signup) | **POST** /auth/signup | Sign up new user


# **auth_signin**
> AuthResponse auth_signin(auth_signin_request)

Sign in user

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import aerostack
from aerostack.models.auth_response import AuthResponse
from aerostack.models.auth_signin_request import AuthSigninRequest
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
    api_instance = aerostack.AuthenticationApi(api_client)
    auth_signin_request = aerostack.AuthSigninRequest() # AuthSigninRequest | 

    try:
        # Sign in user
        api_response = api_instance.auth_signin(auth_signin_request)
        print("The response of AuthenticationApi->auth_signin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_signin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_signin_request** | [**AuthSigninRequest**](AuthSigninRequest.md)|  | 

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User authenticated successfully |  -  |
**401** | Invalid credentials |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_signup**
> AuthResponse auth_signup(auth_signup_request)

Sign up new user

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
import os
import aerostack
from aerostack.models.auth_response import AuthResponse
from aerostack.models.auth_signup_request import AuthSignupRequest
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
    api_instance = aerostack.AuthenticationApi(api_client)
    auth_signup_request = aerostack.AuthSignupRequest() # AuthSignupRequest | 

    try:
        # Sign up new user
        api_response = api_instance.auth_signup(auth_signup_request)
        print("The response of AuthenticationApi->auth_signup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_signup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_signup_request** | [**AuthSignupRequest**](AuthSignupRequest.md)|  | 

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User created successfully |  -  |
**400** |  |  -  |
**409** | User already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

