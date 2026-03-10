from typing import Optional, Dict, List, Any, Union
from aerostack.api_client import ApiClient
from aerostack.configuration import Configuration
from aerostack.api.database_api import DatabaseApi
from aerostack.api.authentication_api import AuthenticationApi
from aerostack.api.cache_api import CacheApi
from aerostack.api.queue_api import QueueApi
from aerostack.api.storage_api import StorageApi
from aerostack.api.ai_api import AIApi
from aerostack.api.services_api import ServicesApi
from aerostack.api.gateway_api import GatewayApi
from aerostack.models.db_query_request import DbQueryRequest
from aerostack.realtime import Realtime

class DatabaseFacade:
    def __init__(self, api: DatabaseApi):
        self._api = api
    
    def dbQuery(self, 
                sql: Optional[str] = None, 
                params: Optional[List[Any]] = None, 
                request: Optional[Dict[str, Any]] = None,
                db_query_request: Optional[DbQueryRequest] = None):
        """
        Ergonomic database query method.
        Supports both direct arguments and Speakeasy-style 'request' dict.
        """
        if db_query_request:
            return self._api.db_query(db_query_request=db_query_request)
        
        if request:
            # Handle Speakeasy style
            req_data = request.get("request_body") or request
            sql = sql or req_data.get("sql") or req_data.get("query")
            params = params or req_data.get("params") or []
        
        req = DbQueryRequest(sql=sql, params=params or [])
        return self._api.db_query(db_query_request=req)

    def db_query(self, *args, **kwargs):
        """Alias for standard snake_case usage"""
        return self.dbQuery(*args, **kwargs)

class SDK:
    """
    Aerostack SDK Facade for Python.
    Provides a clean, ergonomic API for all Aerostack services.
    """
    def __init__(self, 
                 api_key: Optional[str] = None, 
                 api_key_auth: Optional[str] = None,
                 server_url: str = "https://api.aerostack.dev/v1",
                 max_reconnect_attempts: Optional[int] = None):
        
        key = api_key or api_key_auth
        self.configuration = Configuration(
            host=server_url,
            api_key={'ApiKeyAuth': key} if key else None
        )
        
        self.api_client = ApiClient(self.configuration)
        
        # Facades and APIs
        self.database = DatabaseFacade(DatabaseApi(self.api_client))
        self.authentication = AuthenticationApi(self.api_client)
        self.cache = CacheApi(self.api_client)
        self.queue = QueueApi(self.api_client)
        self.storage = StorageApi(self.api_client)
        self.ai = AIApi(self.api_client)
        self.services = ServicesApi(self.api_client)
        self.gateway = GatewayApi(self.api_client)
        
        # Realtime — Realtime class takes configuration + max_reconnect_attempts
        self.realtime = Realtime(
            configuration=self.configuration,
            max_reconnect_attempts=max_reconnect_attempts or 0,
        )

    def set_api_key(self, api_key: str):
        self.configuration.api_key['ApiKeyAuth'] = api_key
        # APIs share the client/config so no need to re-init unless they cached something

# Alias for backward compatibility
Aerostack = SDK
