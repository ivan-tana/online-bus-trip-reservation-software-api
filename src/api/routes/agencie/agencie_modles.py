from pydantic import BaseModel, Field
from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from api.config import SUPPORTED_COUNTRY


PhoneNumber.supported_regions = SUPPORTED_COUNTRY

class Agencies(BaseModel):
    name: str
    contact_email: EmailStr 
    description: str 
    phone_number:  PhoneNumber
    why_choose_us: str 
    agency_imeages: list[str]
    admin_password: str 
    admin_email: EmailStr
    extra_amenities: str



class Branch(BaseModel):
    agency_id: int
    branch_name: str
    email: EmailStr
    contact_name: str
    phone_number: PhoneNumber