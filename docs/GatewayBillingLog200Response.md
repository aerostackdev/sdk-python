# GatewayBillingLog200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**logged_units** | **int** |  | [optional] 

## Example

```python
from aerostack.models.gateway_billing_log200_response import GatewayBillingLog200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayBillingLog200Response from a JSON string
gateway_billing_log200_response_instance = GatewayBillingLog200Response.from_json(json)
# print the JSON string representation of the object
print GatewayBillingLog200Response.to_json()

# convert the object into a dict
gateway_billing_log200_response_dict = gateway_billing_log200_response_instance.to_dict()
# create an instance of GatewayBillingLog200Response from a dict
gateway_billing_log200_response_form_dict = gateway_billing_log200_response.from_dict(gateway_billing_log200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


