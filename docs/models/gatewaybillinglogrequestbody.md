# GatewayBillingLogRequestBody


## Fields

| Field                                       | Type                                        | Required                                    | Description                                 | Example                                     |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `consumer_id`                               | *str*                                       | :heavy_check_mark:                          | The Consumer ID making the request          | usr_123xyz                                  |
| `api_id`                                    | *str*                                       | :heavy_check_mark:                          | The Developer Gateway API ID being consumed | api_chat_bot                                |
| `metric`                                    | *Optional[str]*                             | :heavy_minus_sign:                          | Optional metric name (default: 'units')     | tokens                                      |
| `units`                                     | *int*                                       | :heavy_check_mark:                          | Amount of usage to log                      | 1500                                        |