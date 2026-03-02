# AuthSignupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 
**name** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from aerostack.models.auth_signup_request import AuthSignupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthSignupRequest from a JSON string
auth_signup_request_instance = AuthSignupRequest.from_json(json)
# print the JSON string representation of the object
print AuthSignupRequest.to_json()

# convert the object into a dict
auth_signup_request_dict = auth_signup_request_instance.to_dict()
# create an instance of AuthSignupRequest from a dict
auth_signup_request_form_dict = auth_signup_request.from_dict(auth_signup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


