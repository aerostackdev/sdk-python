# IngestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Text content to index | 
**id** | **str** | Optional custom ID | [optional] 
**type** | **str** | Category/type of content | 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from aerostack.models.ingest_request import IngestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IngestRequest from a JSON string
ingest_request_instance = IngestRequest.from_json(json)
# print the JSON string representation of the object
print IngestRequest.to_json()

# convert the object into a dict
ingest_request_dict = ingest_request_instance.to_dict()
# create an instance of IngestRequest from a dict
ingest_request_form_dict = ingest_request.from_dict(ingest_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


