import logging

from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from api.helpers import exceptions
from api.helpers.functions import exception_message
from pydantic_core import PydanticCustomError



async def default_error_handler(_: Request, exception: Exception) -> JSONResponse:
    """High level exception handler for all exceptions
    """
    logging.exception(exception)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={'message': 'Unhandled Internal Server Error'}
    )

async def agency_already_exist(_: Request, exception: exceptions.AgencyAlreadyExist):

    logging.exception(exception)
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={'message': exception_message(exception)}
    )

async def request_validation_error(_: Request, exception: RequestValidationError):

    logging.exception(exception)
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            'value': exception_message(exception)[0]['input'],
            'message': exception_message(exception)[0]['msg'],
            'log': exception_message(exception)[0]['loc']
            }
    )


async def login_error(_: Request, exception: exceptions.LoginExeption):

    logging.exception(exception)
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={'message': exception_message(exception)}
    )
async def user_creation_eror(_: Request, exception: exceptions.UserCreationError):

    logging.exception(exception)
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={'message': exception_message(exception)}
    )

# async def slow_internet_connection()


def register_exception_handlers(app: FastAPI) -> None:
    """Add exception handlers to FastAPI app
    """
    app.add_exception_handler(Exception, default_error_handler)
    app.add_exception_handler(exceptions.AgencyAlreadyExist, agency_already_exist)
    app.add_exception_handler(RequestValidationError, request_validation_error)
    app.add_exception_handler(exceptions.LoginExeption, login_error)
    app.add_exception_handler(exceptions.UserCreationError, user_creation_eror)