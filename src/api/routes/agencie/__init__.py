from fastapi import APIRouter, Body
from typing import Annotated

from .modles import AgencyCreationForm


agency = APIRouter(
    tags=['Agencies']
    
)

@agency.get('/')
async def get_agencies():
    return {
        'message': 'hello'
    }

@agency.post('/')
def create_agencie(agency: Annotated[AgencyCreationForm, Body(embed=True)]):
    print(agency.model_dump())
    return agency


@agency.get('/{agency_id}/branch')
async def get_branches(agency_id):
    return agency_id

@agency.get('/{agency_id}/branch/{branch_id}')
async def get_branche(agency_id, branch_id):
    pass