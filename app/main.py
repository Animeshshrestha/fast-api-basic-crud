from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import post_v1_router, post_v2_router

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


app.include_router(post_v1_router, tags=['Posts V1'], prefix='/api/v1/posts')
app.include_router(post_v2_router, tags=['Posts V2'], prefix='/api/v2/posts')


@app.get('/api/healthchecker')
def root():
    return {'message': 'Hello World'}