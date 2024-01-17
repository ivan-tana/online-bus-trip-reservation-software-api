import logging

from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse
from api.helpers import exceptions
from api.helpers.functions import exception_message



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


def register_exception_handlers(app: FastAPI) -> None:
    """Add exception handlers to FastAPI app
    """
    app.add_exception_handler(Exception, default_error_handler)
    app.add_exception_handler(exceptions.AgencyAlreadyExist, agency_already_exist)