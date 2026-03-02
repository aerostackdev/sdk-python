# ConfigureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedding_model** | **str** |  | 

## Example

```python
from aerostack.models.configure_request import ConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureRequest from a JSON string
configure_request_instance = ConfigureRequest.from_json(json)
# print the JSON string representation of the object
print ConfigureRequest.to_json()

# convert the object into a dict
configure_request_dict = configure_request_instance.to_dict()
# create an instance of ConfigureRequest from a dict
configure_request_form_dict = configure_request.from_dict(configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


