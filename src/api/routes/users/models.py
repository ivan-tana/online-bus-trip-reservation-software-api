from pydantic import BaseModel, Field, EmailStr, AnyUrl
from datetime import datetime
from pydantic_extra_types.phone_numbers import PhoneNumber
from ...security import BASIC_USER_PERMISSION





class UserCreationForm(BaseModel):
    first_name: str 
    last_name: str 
    email: EmailStr
    phone_number: PhoneNumber
    permissions: list[str] = BASIC_USER_PERMISSION
    password: str 
    image_url: AnyUrl | None = None
    birthday: datetime | None = None


    model_config = {
        "json_schema_extra": {
            "examples": 
            [
                {
                    "first_name": "Jane",
                    "last_name": "deo",
                    "email": "janedeo@gmail.com",
                    "phone_number": "+237678098765",
                    'password': '1234567890',
                    'image_url': 'https://example.com/images/profile.png',
                    'birthday': '02-04-2000',
                }
            ]

        }
    }


class UserLoginForm(BaseModel):
    email: EmailStr
    password: str 

    model_config = {
        "json_schema_extra": {
            "examples": 
            [
                {
                    "email": "janedeo@gmail.com",
                    'password': '1234567890',

                }
            ]

        }
    }