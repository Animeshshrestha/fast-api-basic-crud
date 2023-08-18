from app.custom_endpoint.views import get_posts, create_post, update_post, get_post, delete_post
from app import CreatePostSchema, PostResponse,\
UpdatePostSchema, ListPostResponse

GET_POSTS_LIST = {
        "url": "/post-list/",
        "endpoint": get_posts,
        "methods": {
            'get': {
                'require_auth': False,
                "response_model":ListPostResponse   
            }
        }
    }