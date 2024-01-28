from typing import Awaitable, Callable
import os
from fastapi import FastAPI
from contextlib import asynccontextmanager





import firebase_admin

 
from firebase_admin import credentials




@asynccontextmanager
async def lifespan(app: FastAPI):
    # before the application starts
    cred = credentials.Certificate(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
    
    firebase_admin.initialize_app(credential=cred)
    


    yield
    # after the requests have been send 



