from typing import Callable, Dict, List, Optional
from app.custom_endpoint.config import POST_ENDPOINT_LISTS


class RouteConfig:
    def __init__(self):
        self.routes = []

    def add_route(self, url: str, endpoint: Callable, methods: Dict[str, Dict]):
        self.routes.append({
            "url": url,
            "endpoint": endpoint,
            "methods": methods
        })

    def get_routes(self) -> List[Dict]: 
        return self.routes
    
route_config = RouteConfig()
for route in POST_ENDPOINT_LISTS:
    route_config.add_route(
        url = route["url"],
        endpoint  = route["endpoint"],
        methods = route["methods"]
    )
