from fastapi import APIRouter, Body, status, Depends
from typing import Annotated
from .models import UserCreationForm, UserLoginForm
from firebase_admin import auth
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from ...firebase import firebase, db
from ...helpers import exceptions
from fastapi.security import OAuth2PasswordRequestForm
from ... import database
from ...database.modles import UserOut
from pydantic import BaseModel
from ...security import (
    oauth2_scheme, 
    TOKEN, get_current_user,
    PASSWORD_REQUEST_FORM, 
    PermissionChecker, 
    BASIC_USER_PERMISSION
)

userRouter = APIRouter(
    tags=['User']
)




#### ROUTES 
@userRouter.post('/')
async def get_user(
    current_user: dict = Depends(
        PermissionChecker(
            required_permissions=BASIC_USER_PERMISSION
        ))):
    return current_user

# signup user
@userRouter.post('/signup')
async def signup(user: UserCreationForm):
    email = user.email
    password = user.password
    try: 
        if auth.get_user_by_email(user.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail={
                'message': f'a user with the email {user.email} already exist'
            })
    finally:
        try:
            f_user = auth.create_user(
                email=email,
                password=password
            )
            db.collection("users").document(f_user.uid).set(user.model_dump())
            return JSONResponse(
                ontent={
                    'message': f'Successfully created user {f_user.uid}'},
                    status_code=status.HTTP_200_OK)    
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail={
                'message': 'error creating user'
            })


@userRouter.post('/login')
def login(user: PASSWORD_REQUEST_FORM):
    try:
       current_user = firebase.auth().sign_in_with_email_and_password(user.username, user.password)
       jwt = current_user['idToken']

       return TOKEN(access_token=jwt)
    except:
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={
           'message': 'error logging in user'
       })
    
#### END ROUTES 