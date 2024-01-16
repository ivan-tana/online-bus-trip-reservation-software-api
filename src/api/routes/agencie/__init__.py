from fastapi import APIRouter, Body
from typing import Annotated

from .modles import AgencyCreationForm, BranchCreation
from api.database import agencie as db
from api.database.modles import Agency, Branch


agency = APIRouter(
    tags=['Agency']
    
)

@agency.get('/')
async def get_agencies():
    return db.get_agencies()

# Agency
@agency.post('/')
def create_agency(agency: Annotated[AgencyCreationForm, Body(embed=True)]):
    # TODO  validate form data 



    data = agency.model_dump()

    # create agency
    try: 
        db.create_agency(Agency(**data))
        return {
            "message": f"{agency.name} created successfuly"
        }
    except: 
        # TODO specify the resone for the error 
        # TODO send the correct response code 
        return {
            "message": f" could not create {agency.name}"
        }
    


#Branch
@agency.get('/{agency_id}/branch')
async def get_branches(agency_id):
    return agency_id

#create branch 
@agency.post('/{agency_id}/branch')
async def create_branch(branch: Annotated[BranchCreation, Body(embed=True)]):
    # TODO  validate form data 



    data = branch.model_dump()

    # create branch
    try: 
        db.create_branch(Branch(**data))
        return {
            "message": f"{branch.name} created successfuly"
        }
    except: 
        # TODO specify the resone for the error 
        # TODO send the correct response code 
        return {
            "message": f" could not create {BranchCreation.name}"
        }


@agency.get('/{agency_id}/branch/{branch_id}')
async def get_branche(agency_id, branch_id):
    pass