# ServicesInvokeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_name** | **str** |  | 
**data** | **Dict[str, object]** |  | 

## Example

```python
from aerostack.models.services_invoke_request import ServicesInvokeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesInvokeRequest from a JSON string
services_invoke_request_instance = ServicesInvokeRequest.from_json(json)
# print the JSON string representation of the object
print ServicesInvokeRequest.to_json()

# convert the object into a dict
services_invoke_request_dict = services_invoke_request_instance.to_dict()
# create an instance of ServicesInvokeRequest from a dict
services_invoke_request_form_dict = services_invoke_request.from_dict(services_invoke_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


