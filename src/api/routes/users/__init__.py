from fastapi import APIRouter, Body, status, Depends
from typing import Annotated
from .models import UserCreationForm, UserLoginForm
from firebase_admin import auth
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from ...firebase import firebase, db
from ...helpers import exceptions
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ... import database
from ...database.modles import UserOut
from pydantic import BaseModel


userRouter = APIRouter(
    tags=['User']
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl='/user/login',
    scopes={'items': 'permissions to access items'}
)


#### MODELS 

class TOKEN(BaseModel):
    access_token: str
    bearer: str = "bearer"

#### END MODELS 


#### DEPENDENCIES

#### DEPENDENCIES

TOKEN_DEP = Annotated[str, Depends(oauth2_scheme)]

#### END DEPENDENCIES

### Functions

async def get_current_user(token: TOKEN_DEP):
    try: 
        user = auth.verify_id_token(token)
        data = database.get_user_data(user['uid'])
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        print(UserOut(**data))
        return data

    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    

async def check_role(role_required: str, user: Annotated[dict, Depends(get_current_user)]):
    if not role_required is user['role']:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions"
        )


#### END FUNCTIONS

#### DEPENDENCIES

CURRENT_USER = Annotated[dict, Depends(get_current_user)]
PASSWORD_REQUEST_FORM = Annotated[OAuth2PasswordRequestForm, Depends()]

#### END DEPENDENCIES

#### ROUTES 
@userRouter.post('/')
async def get_user(current_user: dict = Depends(get_current_user)):
    return current_user

# signup user
@userRouter.post('/signup')
async def signup(user: UserCreationForm):
    email = user.email
    password = user.password
    try: 
        if auth.get_user_by_email(user.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={
                'message': f'a user with the email {user.email} already exist'
            })
    finally:
        try:
            f_user = auth.create_user(
                email=email,
                password=password
            )
            db.collection("users").document(f_user.uid).set(user.model_dump())
            return JSONResponse(content={'message': f'Successfully created user {f_user.uid}'}, status_code=status.HTTP_200_OK)    
        except:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={
                'message': 'error creating user'
            })


@userRouter.post('/login')
def login(user: PASSWORD_REQUEST_FORM):
    try:
       print(user.username, user.password)
       current_user = firebase.auth().sign_in_with_email_and_password(user.username, user.password)
       jwt = current_user['idToken']

       return TOKEN(access_token=jwt)
    except:
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={
           'message': 'error logging in user'
       })
    
#### END ROUTES 