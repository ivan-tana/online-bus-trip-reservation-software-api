from typing import Awaitable, Callable
import os
from fastapi import FastAPI
from contextlib import asynccontextmanager


import firebase_admin
import pyrebase
import json
 
from firebase_admin import credentials
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException


@asynccontextmanager
async def lifespan(app: FastAPI):
    # before the application starts
    cred = credentials.Certificate(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
    firebase_admin.initialize_app(credential=cred)
    pb = pyrebase.initialize_app(json.load(open(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])))

    allow_all = ['*']
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_all,
        allow_credentials=True,
        allow_methods=allow_all,
        allow_headers=allow_all
    )
    yield
    # after the requests have been send 



