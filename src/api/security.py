from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field, EmailStr, AnyUrl
from typing import Annotated
from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from firebase_admin import auth
from .database import (
    USER_FROM_TOKEN
)


from . import database

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl='/user/login',
    scopes={}
)


### Variables 
BASIC_USER_PERMISSION = ['user:read', 'user:write']
### END Variables 

#### MODELS 

class TOKEN(BaseModel):
    access_token: str
    token_type: str = "bearer"

class USER_AUTH(BaseModel):
    permissions: list[str] = []


#### END MODELS 


#### DEPENDENCIES

TOKEN_DEP = Annotated[str, Depends(oauth2_scheme)]


#### END DEPENDENCIES


### Functions

async def get_current_user(token: TOKEN_DEP):
    try: 
        data = USER_FROM_TOKEN(token).data
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


### CLASS
class PermissionChecker:

    def __init__(self, required_permissions: list[str]) -> None:
        self.required_permissions = required_permissions

    def __call__(self, user: USER_AUTH = Depends(get_current_user)) -> bool:
        for r_perm in self.required_permissions:
            if r_perm not in user['permissions']:
                raise HTTPException(
                    status_code=status.HTTP_401_NAUTHORIZED,
                    detail='Invalid Permissions'
                )
        return user
### END CLASS