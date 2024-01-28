from pydantic import BaseModel, Field, EmailStr, AnyUrl
from datetime import datetime
from pydantic_extra_types.phone_numbers import PhoneNumber





class UserCreationForm(BaseModel):
    first_name: str 
    last_name: str 
    email: EmailStr
    phone_number: PhoneNumber
    password: str 
    role: str | None # convert to enum with the roles [super_admin, branch_admin, employee]
    created_at: datetime = Field(default_factory=datetime.now)
    image_url: AnyUrl | None = None
    birthday: datetime | None = None
    agency_id: str | None = None
    branch_id: str | None = None
    is_admin: bool = False


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
                    'role': 'branch_admin',
                    'created_at': datetime.now(),
                    'image_url': 'https://example.com/images/profile.png',
                    'birthday': '02-04-2000',
                    'agency_id': 1,
                    'branch_id': 4,
                    'is_admin': True
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