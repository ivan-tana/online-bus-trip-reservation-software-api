
# agency
from fastapi.exceptions import HTTPException

class AgencyError(Exception):
    message = "An error with the agency request"

class AgencyAlreadyExist(AgencyError):
    message = "Agency already exist"



# login/signup 
    
class LoginExeption(Exception):
    message = "Error logging in user"

class UserCreationError(Exception):
    message = "Error creating a user"
