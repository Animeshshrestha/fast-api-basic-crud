from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from app.routers import post_v1_router, post_v2_router
from app.custom_endpoint.configuration import route_config

app = FastAPI()

# origins = [
#     settings.CLIENT_ORIGIN,
# ]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# app.include_router(post_v1_router, tags=['Posts V1'], prefix='/api/v1/posts')
# app.include_router(post_v2_router, tags=['Posts V2'], prefix='/api/v2/posts')
for route in route_config.get_routes():
    for method, settings in route["methods"].items():
        dependencies = []
        
        if settings.get("require_auth", False):
            pass
            # dependencies.append(Depends(authorization.get_current_user))
        app.router.add_api_route(
            path=route["url"],
            endpoint=route["endpoint"],
            methods=[method.upper()],
            response_model=settings.get("response_model", None),
            dependencies=dependencies
        )


@app.get('/api/healthchecker')
def root():
    return {'message': 'Hello World'}