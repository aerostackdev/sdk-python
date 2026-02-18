from .types import Hooks, BeforeRequestHook, BeforeRequestContext
import httpx

# Persistent state for project ID
_global_project_id = None

def set_project_id(project_id: str):
    """Set the project ID for all SDK requests."""
    global _global_project_id
    _global_project_id = project_id

class ProjectIdHook(BeforeRequestHook):
    def before_request(self, hook_ctx: BeforeRequestContext, request: httpx.Request) -> httpx.Request:
        if _global_project_id:
            request.headers["X-Project-Id"] = _global_project_id
        return request

def init_hooks(hooks: Hooks):
    hooks.register_before_request_hook(ProjectIdHook())
