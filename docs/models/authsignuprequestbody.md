# AuthSignupRequestBody


## Fields

| Field              | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `email`            | *str*              | :heavy_check_mark: | N/A                | user@example.com   |
| `password`         | *str*              | :heavy_check_mark: | N/A                | SecurePass123!     |
| `name`             | *Optional[str]*    | :heavy_minus_sign: | N/A                | John Doe           |
| `metadata`         | Dict[str, *Any*]   | :heavy_minus_sign: | N/A                |                    |