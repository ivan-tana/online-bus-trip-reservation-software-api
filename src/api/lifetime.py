from fastapi import FastAPI
from contextlib import asynccontextmanager










@asynccontextmanager
async def lifespan(app: FastAPI):
    # before the application starts
    yield
    # after the requests have been send 



