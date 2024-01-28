from fastapi import APIRouter, Body
from typing import Annotated

from .modles import AgencyCreationForm, BranchCreation, AgencyUpdateForm, BranchUpdate
from ...database import agencie as db



Agency = APIRouter(
    tags=['Agency']
    
)

@Agency.get('/')
async def get_agencies():
    return db.get_agencies()

# Agency
@Agency.post('/')
def create_agency(agency: Annotated[AgencyCreationForm, Body(embed=True)]):
    data = agency.model_dump(exclude_none=True)
    db.create_agency(data)
    return {
        "message": f"{agency.name} created successfuly"
    }



@Agency.put('/')
def update_agency(agency: Annotated[AgencyUpdateForm, Body(embed=True)]):
    data = agency.model_dump(exclude_none=True)
    db.update_agency(data)
    return {
        "messsage": "Updated successfully"
    }


#Branch
@Agency.get('/{agency_id}/branch')
async def get_branches(agency_id):
    return agency_id

#create branch 
@Agency.post('/{agency_id}/branch')
async def create_branch(branch: Annotated[BranchCreation, Body(embed=True)]):
    data = branch.model_dump(exclude_none=True)
    db.create_branch(data)
    return {
        "message": f"{branch.name} created successfuly"
    }

# update branch 
@Agency.put('/{agency_id}/branch/{branch_id}')
async def update_branch(branch: Annotated[BranchUpdate, Body(embed=True)], agency_id, branch_id):
    data = branch.model_dump(exclude_none=True)
    db.update_branch(data, agency_id, branch_id)
    return {
        'message': 'branch updated'
    }



@Agency.get('/{agency_id}/branch/{branch_id}')
async def get_branche(agency_id, branch_id):
    pass