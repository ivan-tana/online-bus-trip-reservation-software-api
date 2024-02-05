from fastapi import APIRouter, Body
from typing import Annotated

from .modles import AgencyCreationForm, BranchCreation, AgencyUpdateForm, BranchUpdate
from ... import database as db
from ...security import PermissionChecker, BASIC_USER_PERMISSION, CURRENT_USER


Agency = APIRouter(
    tags=['Agency']
    
)

@Agency.get('/')
async def get_agencies(
    user: CURRENT_USER,
):
    return db.get_agencies()

# Agency
@Agency.post('/')
def create_agency(
    user: CURRENT_USER,
    agency: Annotated[AgencyCreationForm, Body(embed=True)]
    
    ):
    data = agency.model_dump(exclude_none=True)
    email = db.create_agency(data)
    db.update_user(user_id=user['id'],data={"agency_id": email})
    return {
        "message": f"{agency.name} created successfuly"
    }



@Agency.put('/')
def update_agency(
    user: CURRENT_USER,
    agency: Annotated[AgencyUpdateForm, Body(embed=True)]
    ):
    data = agency.model_dump(exclude_none=True)
    db.update_agency(data)
    return {
        "messsage": "Updated successfully"
    }


#Branch
@Agency.get('/{agency_id}/branch')
async def get_branches(
    user: CURRENT_USER,
    agency_id
    ):
    return agency_id

#create branch 
@Agency.post('/{agency_id}/branch')
async def create_branch(
    user: CURRENT_USER,
    branch: Annotated[BranchCreation, Body(embed=True)]
    ):
    data = branch.model_dump(exclude_none=True)
    db.create_branch(data)
    return {
        "message": f"{branch.name} created successfuly"
    }

# update branch 
@Agency.put('/{agency_id}/branch/{branch_id}')
async def update_branch(
    user: CURRENT_USER,
    branch: Annotated[BranchUpdate, Body(embed=True)], agency_id, branch_id
    ):
    data = branch.model_dump(exclude_none=True)
    db.update_branch(data, agency_id, branch_id)
    return {
        'message': 'branch updated'
    }



@Agency.get('/{agency_id}/branch/{branch_id}')
async def get_branche(
    user: CURRENT_USER,
    agency_id,
    branch_id
    ):
    pass