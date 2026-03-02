# QueueEnqueue201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from aerostack.models.queue_enqueue201_response import QueueEnqueue201Response

# TODO update the JSON string below
json = "{}"
# create an instance of QueueEnqueue201Response from a JSON string
queue_enqueue201_response_instance = QueueEnqueue201Response.from_json(json)
# print the JSON string representation of the object
print QueueEnqueue201Response.to_json()

# convert the object into a dict
queue_enqueue201_response_dict = queue_enqueue201_response_instance.to_dict()
# create an instance of QueueEnqueue201Response from a dict
queue_enqueue201_response_form_dict = queue_enqueue201_response.from_dict(queue_enqueue201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


