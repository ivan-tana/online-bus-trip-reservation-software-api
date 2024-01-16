
from .modles import Agency, Branch

# create 
def  create_agency(agency: Agency):
    data = agency.model_dump()
    

def create_branch(branch: Branch):
    data = branch.model_dump()


# retrive 


def get_agencies():
    return [
        {
            "name": "mogamo",
            "email": "info@mogamo.com",
            "phone_number": "+237-674-234-253-324"

        }
    ]