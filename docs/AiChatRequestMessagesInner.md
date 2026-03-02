# AiChatRequestMessagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from aerostack.models.ai_chat_request_messages_inner import AiChatRequestMessagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatRequestMessagesInner from a JSON string
ai_chat_request_messages_inner_instance = AiChatRequestMessagesInner.from_json(json)
# print the JSON string representation of the object
print AiChatRequestMessagesInner.to_json()

# convert the object into a dict
ai_chat_request_messages_inner_dict = ai_chat_request_messages_inner_instance.to_dict()
# create an instance of AiChatRequestMessagesInner from a dict
ai_chat_request_messages_inner_form_dict = ai_chat_request_messages_inner.from_dict(ai_chat_request_messages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


