from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from pydantic_extra_types.phone_numbers import PhoneNumber

class Agency(BaseModel):
    name: str
    contact_email: EmailStr 
    description: str 
    phone_number:  PhoneNumber
    why_choose_us: str 
    agency_images: list[str] | None
    website: str | None

class Branch(BaseModel):
    agency_id: str
    branch_name: str
    email: EmailStr
    contact_name: str
    phone_number: PhoneNumber


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone_number: PhoneNumber
    password: str 
    role: str | None # convert to enum with the roles [super_admin, branch_admin, employee]
    created_at: datetime = Field(default_factory=datetime.now)
    image_url: str = None   
    DoB: datetime = None 
    agency_id: str = None 
    branch_id: str = None 
    is_admin: bool = False

class Trip(BaseModel):
    id: int
    agency_id: int
    origin: str
    destination: str
    departure_date: datetime
    departure_time: str
    price: float
    bus_category: str
    bus_number: str
    bus_type: str
    available_seats_left: int

class Booking(BaseModel):
    id: int
    user_id: int
    trip_id: int
    payment_method: str
    transaction_id: str
    booked_at: datetime = Field(default_factory=datetime.now)
    status: str



# Additional models for future updates:

class Review(BaseModel):
    id: int
    user_id: int
    trip_id: int
    rating: int
    review_text: str

class Location(BaseModel):
    id: int
    city: str
    region: str

class Payment(BaseModel):
    id: int
    booking_id: int
    payment_gateway: str
    payment_details: str
