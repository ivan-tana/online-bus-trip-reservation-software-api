from fastapi import APIRouter, Body, status, Depends
from .models import UserCreationForm
from fastapi.exceptions import HTTPException
from ...firebase import firebase, db
from ... import database
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
    user = database.CreateUser(user.model_dump(exclude_none=True))
    return {
        'message': 'user has be created'
    }


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