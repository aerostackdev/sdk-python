# DbQueryRequestBody


## Fields

| Field                                    | Type                                     | Required                                 | Description                              | Example                                  |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `sql`                                    | *str*                                    | :heavy_check_mark:                       | SQL query to execute                     | SELECT * FROM users WHERE active = ?     |
| `params`                                 | List[*Any*]                              | :heavy_minus_sign:                       | Query parameters for prepared statements | [<br/>true<br/>]                         |