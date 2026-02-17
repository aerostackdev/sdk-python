from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from aerostack import Aerostack
import json
import os

"""
Django Integration Example

Demonstrates how to use the Aerostack Python SDK in a Django View.
"""

# Initialize SDK globally or inside usage as preferred
sdk = Aerostack(
    # api_key_auth=os.environ.get("AEROSTACK_API_KEY")
)

@method_decorator(csrf_exempt, name='dispatch')
class AerostackAuthView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            name = data.get('name')

            res = sdk.authentication.auth_signup(
                request={
                    "email": email,
                    "password": password,
                    "name": name
                }
            )

            # Assuming res.auth_signup_response is a Pydantic model or dict
            return JsonResponse(res.auth_signup_response.__dict__, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

class DatabaseView(View):
    def get(self, request):
        try:
            res = sdk.database.db_query(
                request={"query": "SELECT * FROM users LIMIT 5"}
            )
            return JsonResponse(res.db_query_response, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
