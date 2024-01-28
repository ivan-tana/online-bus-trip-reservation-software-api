
from api.helpers import exceptions


agencies  = [
    {
        "name": "mogamo",
        "contact_email": "info@mogamo.com",
        "phone_number": "+237-674-234-253-324",
        "why_choose_us": "",
        "description": "",
        "agency_images": []
    },
        {
        "name": "Garnatie",
        "contact_email": "info@mogamo.com",
        "phone_number": "+237-674-234-253-324",
        "why_choose_us": "",
        "description": "",
        "agency_images": []
    }
]


# create 
def  create_agency(data: dict):
    # raise exceptions.AgencyAlreadyExist(f"an agency with the name {data['name']} already exist")
    
    try:
        agencies.append(data)
        return True
    except:
        return False

def create_branch(data: dict):
    print(data)


# retrive 


def get_agencies():
    return agencies


# update 
def update_agency(data: dict):
    print(data)


def update_branch(data: dict, agency_id: int, branch_id: int):
    print(data)