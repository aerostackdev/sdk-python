# AiChatRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | [optional] 
**messages** | [**List[AiChatRequestMessagesInner]**](AiChatRequestMessagesInner.md) |  | 

## Example

```python
from aerostack.models.ai_chat_request import AiChatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatRequest from a JSON string
ai_chat_request_instance = AiChatRequest.from_json(json)
# print the JSON string representation of the object
print AiChatRequest.to_json()

# convert the object into a dict
ai_chat_request_dict = ai_chat_request_instance.to_dict()
# create an instance of AiChatRequest from a dict
ai_chat_request_form_dict = ai_chat_request.from_dict(ai_chat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


