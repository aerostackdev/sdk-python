# DbQueryResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **List[Dict[str, object]]** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from aerostack.models.db_query_result import DbQueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of DbQueryResult from a JSON string
db_query_result_instance = DbQueryResult.from_json(json)
# print the JSON string representation of the object
print DbQueryResult.to_json()

# convert the object into a dict
db_query_result_dict = db_query_result_instance.to_dict()
# create an instance of DbQueryResult from a dict
db_query_result_form_dict = db_query_result.from_dict(db_query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


