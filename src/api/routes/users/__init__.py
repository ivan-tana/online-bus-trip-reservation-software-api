from fastapi import APIRouter, Body, status
from typing import Annotated
from .models import UserCreationForm, UserLoginForm
from firebase_admin import auth
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from api.firebase import pb
from api.helpers import exceptions


userRouter = APIRouter(
    tags=['User']
)




@userRouter.post('/')
def get_user():
    return {
        "user": "john deo"
    }


# signup user
@userRouter.post('/signup')
async def signup(user: UserLoginForm):
    email = user.email
    password = user.password
    try: 
        if auth.get_user_by_email(user.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={
                'message': f'a user with the email {user.email} already exist'
            })
    finally:
        try:
            user = auth.create_user(
                email=email,
                password=password
            )
            return JSONResponse(content={'message': f'Successfully created user {user.uid}'}, status_code=status.HTTP_200_OK)    
        except:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={
                'message': 'error creating user'
            })


@userRouter.post('/login')
def login(user: Annotated[UserLoginForm, Body(embed=True)]):


    try:
       
       current_user = pb.auth().sign_in_with_email_and_password(user.email, user.password)
       jwt = current_user['idToken']
       return JSONResponse(content={'token': jwt}, status_code=status.HTTP_200_OK)
    except:
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={
           'message': 'error logging in user'
       })