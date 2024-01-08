from fastapi import APIRouter, Body
from typing import Annotated

from .agencie_modles import Agencies


agencie = APIRouter(
    tags=['Agencies']
    
)

@agencie.get('/')
async def get_agencies():
    return {
        'message': 'hello'
    }

@agencie.post('/')
def create_agencie(agencie: Annotated[Agencies, Body(embed=True)]):
    return agencie