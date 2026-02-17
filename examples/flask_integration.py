from flask import Flask, request, jsonify
from aerostack import Aerostack
import os

"""
Flask Integration Example

Demonstrates how to use the Aerostack Python SDK within a Flask application.
"""

app = Flask(__name__)

# Initialize SDK
# In production, use os.environ to load API key
sdk = Aerostack(
    # api_key_auth=os.environ.get("AEROSTACK_API_KEY") 
)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')

    try:
        # Call Aerostack Auth API
        res = sdk.authentication.auth_signup(
            request={
                "email": email,
                "password": password,
                "name": name
            }
        )

        if res.status_code == 201:
            return jsonify(res.auth_signup_response), 201
        else:
            return jsonify({"error": "Signup failed"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/users', methods=['GET'])
def list_users():
    try:
        # Call Aerostack DB API (binding-like usage via HTTP)
        res = sdk.database.db_query(
            request={
                "query": "SELECT * FROM users LIMIT 10"
            }
        )
        
        return jsonify(res.db_query_response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=3000, debug=True)
