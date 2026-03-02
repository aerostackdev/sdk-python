# QueueEnqueueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**data** | **Dict[str, object]** |  | 
**delay** | **int** | Delay in seconds before processing | [optional] 

## Example

```python
from aerostack.models.queue_enqueue_request import QueueEnqueueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueueEnqueueRequest from a JSON string
queue_enqueue_request_instance = QueueEnqueueRequest.from_json(json)
# print the JSON string representation of the object
print QueueEnqueueRequest.to_json()

# convert the object into a dict
queue_enqueue_request_dict = queue_enqueue_request_instance.to_dict()
# create an instance of QueueEnqueueRequest from a dict
queue_enqueue_request_form_dict = queue_enqueue_request.from_dict(queue_enqueue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


