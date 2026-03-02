# ServicesInvoke200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**result** | **object** |  | [optional] 

## Example

```python
from aerostack.models.services_invoke200_response import ServicesInvoke200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesInvoke200Response from a JSON string
services_invoke200_response_instance = ServicesInvoke200Response.from_json(json)
# print the JSON string representation of the object
print ServicesInvoke200Response.to_json()

# convert the object into a dict
services_invoke200_response_dict = services_invoke200_response_instance.to_dict()
# create an instance of ServicesInvoke200Response from a dict
services_invoke200_response_form_dict = services_invoke200_response.from_dict(services_invoke200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


