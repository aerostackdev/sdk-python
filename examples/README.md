# Aerostack Python SDK Examples

Examples for `aerostack` (Python).

## Prerequisites

```bash
pip install aerostack
```

## Available Examples

| Example | Description | Framework |
|---------|-------------|-----------|
| [**Flask Integration**](./flask_integration.py) | Simple route handler in Flask. | Flask |
| [**FastAPI Integration**](./fastapi_integration.py) | Using Dependency Injection for SDK. | FastAPI |
| [**Django Integration**](./django_integration.py) | Class-based view integration. | Django |

## Usage

### Running Flask Example

```bash
# Install flask
pip install flask

# Run
python examples/flask_integration.py
```

### Running FastAPI Example

```bash
# Install fastapi uvicorn
pip install fastapi uvicorn

# Run
uvicorn examples.fastapi_integration:app --reload
```
