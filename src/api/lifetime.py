from typing import Awaitable, Callable
from typing import Dict, Iterable, Optional, Union
from types import ModuleType
import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from contextlib import AbstractAsyncContextManager, asynccontextmanager
import firebase_admin
from firebase_admin import credentials
from tortoise.contrib.fastapi import register_tortoise
from tortoise.exceptions import DoesNotExist, IntegrityError
from tortoise import Tortoise, connections
from tortoise.log import logger
from api.config import TORTOISE_ORM




def register_tortoise(
    app: FastAPI,
    config: Optional[dict] = None,
    config_file: Optional[str] = None,
    db_url: Optional[str] = None,
    modules: Optional[Dict[str, Iterable[Union[str, ModuleType]]]] = None,
    generate_schemas: bool = False,
    add_exception_handlers: bool = False,
) -> AbstractAsyncContextManager:
    async def init_orm() -> None:  # pylint: disable=W0612
        await Tortoise.init(config=config, config_file=config_file, db_url=db_url, modules=modules)
        logger.info("Tortoise-ORM started, %s, %s", connections._get_storage(), Tortoise.apps)
        if generate_schemas:
            logger.info("Tortoise-ORM generating schema")
            await Tortoise.generate_schemas()

    async def close_orm() -> None:  # pylint: disable=W0612
        await connections.close_all()
        logger.info("Tortoise-ORM shutdown")

    class Manager(AbstractAsyncContextManager):
        async def __aenter__(self) -> "Manager":
            await init_orm()
            return self

        async def __aexit__(self, *args, **kwargs) -> None:
            await close_orm()

    if add_exception_handlers:

        @app.exception_handler(DoesNotExist)
        async def doesnotexist_exception_handler(request: Request, exc: DoesNotExist):
            return JSONResponse(status_code=404, content={"detail": str(exc)})

        @app.exception_handler(IntegrityError)
        async def integrityerror_exception_handler(request: Request, exc: IntegrityError):
            return JSONResponse(
                status_code=422,
                content={"detail": [{"loc": [], "msg": str(exc), "type": "IntegrityError"}]},
            )

    return Manager()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # before the application starts
    cred = credentials.Certificate(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
    firebase_admin.initialize_app(credential=cred)

    async with register_tortoise(
        app,
        db_url=TORTOISE_ORM['connections']['default'],
        modules={"models": ["api.database.modles"]},
        generate_schemas=True,
        add_exception_handlers=True,
    ):
        # do sth while db connected
        yield
    yield
    # after the requests have been send 
    await Tortoise.close_connections()



