# DbQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sql** | **str** | SQL query to execute | 
**params** | **List[object]** | Query parameters for prepared statements | [optional] 

## Example

```python
from aerostack.models.db_query_request import DbQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DbQueryRequest from a JSON string
db_query_request_instance = DbQueryRequest.from_json(json)
# print the JSON string representation of the object
print DbQueryRequest.to_json()

# convert the object into a dict
db_query_request_dict = db_query_request_instance.to_dict()
# create an instance of DbQueryRequest from a dict
db_query_request_form_dict = db_query_request.from_dict(db_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


