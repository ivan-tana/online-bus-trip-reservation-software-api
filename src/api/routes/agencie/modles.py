from pydantic import BaseModel, Field, field_serializer
from pydantic import EmailStr, AnyUrl
from pydantic_extra_types.phone_numbers import PhoneNumber



class AgencyCreationForm(BaseModel):
    name: str
    contact_email: EmailStr 
    description: str 
    phone_number:  PhoneNumber
    why_choose_us: str | None = None
    agency_images: list[AnyUrl] | None = None


    @field_serializer('agency_images')
    def serialize_url(agency_images: list[AnyUrl]) -> list[str]:
        result = []
        for item in agency_images:
            result.append(str(item))
        return result

    model_config = {
        "json_schema_extra": {
            "examples": 
            [
                {
                    "name": "Mogamo",
                    "contact_email": "info@mogamo.com",
                    "description": "The Best travel agency in cameroon",
                    "phone_number": "+237678098765",
                    "why_choose_us": "Best customer service",
                    "agency_images": [
                        "https://mogamo.com/images/park.png"
                    ]           
                }
            ]

        }
    }

class AgencyUpdateForm(BaseModel):
    name: str | None = None
    contact_email: EmailStr | None = None
    description: str | None = None
    phone_number:  PhoneNumber | None = None
    why_choose_us: str | None = None
    agency_images: list[AnyUrl] | None = None

class Locatiion(BaseModel):
    country: str 
    region : str 
    city: str 
    geo_location: list[float] | None = None
    model_config = {
        "json_schema_extra": {
            "examples": 
            [
                {
                    "country": "Mogamo",
                    "region": "South West",
                    "geo_location": [
                        92.34, 123.32
                    ],
                    "city": "Kumba Town",       
                }
            ]

        }
    }

class BranchCreation(BaseModel):
    agency_id: int 
    name: str | None = None
    location : Locatiion 
    momo_phone_number: PhoneNumber
    description: str 
    images: list[AnyUrl] | None = None
    email: EmailStr
    contact_phone_number: PhoneNumber

    model_config = {
        "json_schema_extra": {
            "examples": 
            [
                {
                    "agency_id": 1,
                    "name": "Mogamo Kumba Branch",
                    "location": {
                    "country": "Cameroon",
                    "region": "South west",
                    "city": "Kumba Town",
                    "geo_location": [
                        92.34, 123.32
                    ]
                    },
                    "momo_phone_number": "+237789087962",
                    "description": "Mogamo kumba branch",
                    "images": [
                        "https://mogamo.com/images/park.png"
                        ],
                    "email": "kumba@mogamo.com",
                    "contact_phone_number": "+237789087962"          
                }
            ]

        }
    }

class BranchUpdate(BaseModel):
    name: str | None = None
    location : Locatiion | None = None
    momo_phone_number: PhoneNumber | None = None
    description: str | None = None
    images: list[AnyUrl] | None = None
    email: EmailStr | None = None
    contact_phone_number: PhoneNumber | None = None






