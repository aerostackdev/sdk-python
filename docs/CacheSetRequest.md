# CacheSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | **object** |  | 
**ttl** | **int** | Time to live in seconds | [optional] 

## Example

```python
from aerostack.models.cache_set_request import CacheSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CacheSetRequest from a JSON string
cache_set_request_instance = CacheSetRequest.from_json(json)
# print the JSON string representation of the object
print CacheSetRequest.to_json()

# convert the object into a dict
cache_set_request_dict = cache_set_request_instance.to_dict()
# create an instance of CacheSetRequest from a dict
cache_set_request_form_dict = cache_set_request.from_dict(cache_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


