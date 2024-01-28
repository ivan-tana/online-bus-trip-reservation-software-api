from fastapi import APIRouter, Body
from typing import Annotated
from .models import UserCreationForm, UserLoginForm


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
def signup(user: Annotated[UserCreationForm, Body(embed=True)]): 
    return user


@userRouter.post('/login')
def login(user: Annotated[UserLoginForm, Body(embed=True)]):
    return user