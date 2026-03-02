# AuthSigninRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from aerostack.models.auth_signin_request import AuthSigninRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthSigninRequest from a JSON string
auth_signin_request_instance = AuthSigninRequest.from_json(json)
# print the JSON string representation of the object
print AuthSigninRequest.to_json()

# convert the object into a dict
auth_signin_request_dict = auth_signin_request_instance.to_dict()
# create an instance of AuthSigninRequest from a dict
auth_signin_request_form_dict = auth_signin_request.from_dict(auth_signin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


