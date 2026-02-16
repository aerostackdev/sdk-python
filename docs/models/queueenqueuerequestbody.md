# QueueEnqueueRequestBody


## Fields

| Field                              | Type                               | Required                           | Description                        | Example                            |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `type`                             | *str*                              | :heavy_check_mark:                 | N/A                                | send-email                         |
| `data`                             | Dict[str, *Any*]                   | :heavy_check_mark:                 | N/A                                |                                    |
| `delay`                            | *Optional[int]*                    | :heavy_minus_sign:                 | Delay in seconds before processing | 60                                 |