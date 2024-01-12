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





