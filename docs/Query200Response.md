# Query200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 

## Example

```python
from aerostack.models.query200_response import Query200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Query200Response from a JSON string
query200_response_instance = Query200Response.from_json(json)
# print the JSON string representation of the object
print Query200Response.to_json()

# convert the object into a dict
query200_response_dict = query200_response_instance.to_dict()
# create an instance of Query200Response from a dict
query200_response_form_dict = query200_response.from_dict(query200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


