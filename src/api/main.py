from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from fastapi.routing import APIRouter

from api.routes.user import user
from api.routes.agencie import agencie
from api.lifetime import lifespan
from api.exception_handlers import register_exception_handlers


def get_app() -> FastAPI:
    """Get API app
    """
    app = FastAPI(
        lifespan=lifespan
        title='online bus trip reservation',
        description="""
        This API powers an online bus trip reservation platform designed to streamline the booking process
        or travelers and simplify trip management for bus operators. Our mission is to eliminate the hassle, 
        financial burden, and wasted time associated with traditional inter-urban bus travel booking
        """,
        docs_url='/api/docs',
        redoc_url='/api/redoc',
        openapi_url='/api/openapi.json',
        default_response_class=UJSONResponse,
    )


    # Adds startup and shutdown events.
    register_exception_handlers(app)

    api_router = APIRouter()
    api_router.include_router(user, prefix='/user', tags=['users'])
    
    
    app.include_router(router=api_router, prefix='/api')
    app.include_router(router=agencie, prefix='/agencie')

    return app
