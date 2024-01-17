
# agency


class AgencyError(Exception):
    message = "An error with the agency request"

class AgencyAlreadyExist(AgencyError):
    message = "Agency already exist"