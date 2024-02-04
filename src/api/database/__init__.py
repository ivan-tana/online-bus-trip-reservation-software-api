
from ..helpers import exceptions
from ..firebase import db


# create 
def  create_agency(data: dict):
    # raise exceptions.AgencyAlreadyExist(f"an agency with the name {data['name']} already exist")
    pass

def create_branch(data: dict):
    pass

# retrive 


def get_user_data(uid: str):

    doc_ref = db.collection('users').document(uid).get() 
    
    if doc_ref.exists:
        data = doc_ref.to_dict()
    else:
        data = {}
    return data


# update 
def update_agency(data: dict):
    print(data)


def update_branch(data: dict, agency_id: int, branch_id: int):
    print(data)