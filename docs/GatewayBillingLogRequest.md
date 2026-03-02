# GatewayBillingLogRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_id** | **str** | The Consumer ID making the request | 
**api_id** | **str** | The Developer Gateway API ID being consumed | 
**metric** | **str** | Optional metric name (default: &#39;units&#39;) | [optional] 
**units** | **int** | Amount of usage to log | 

## Example

```python
from aerostack.models.gateway_billing_log_request import GatewayBillingLogRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayBillingLogRequest from a JSON string
gateway_billing_log_request_instance = GatewayBillingLogRequest.from_json(json)
# print the JSON string representation of the object
print GatewayBillingLogRequest.to_json()

# convert the object into a dict
gateway_billing_log_request_dict = gateway_billing_log_request_instance.to_dict()
# create an instance of GatewayBillingLogRequest from a dict
gateway_billing_log_request_form_dict = gateway_billing_log_request.from_dict(gateway_billing_log_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


