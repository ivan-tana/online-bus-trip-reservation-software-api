from pydantic import BaseModel
from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from api.config import SUPPORTED_COUNTRY


PhoneNumber.supported_regions = SUPPORTED_COUNTRY

class AgencyCreationForm(BaseModel):
    name: str
    contact_email: EmailStr 
    description: str 
    phone_number:  PhoneNumber
    why_choose_us: str 
    agency_imeages: list[str]

class Locatiion(BaseModel):
    country: str 
    region : str 
    city: str 
    street: str 
    geo_location: list

class BranchCreation(BaseModel):
    name: str | None 
    location : Locatiion 
    momo_phone_number: PhoneNumber
    description: str 
    images: list
    email: EmailStr
    contact_phone_number: PhoneNumber








