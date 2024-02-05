from ..firebase import db
from firebase_admin import auth
from fastapi.exceptions import HTTPException
from fastapi import status
from firebase_admin._auth_utils import (
    UserNotFoundError,
    InvalidIdTokenError,
)
from firebase_admin._token_gen import ExpiredIdTokenError, RevokedIdTokenError



AGENCY_COLLECTION  = db.collection('agencies')
USERS_COLLECTION = 'users'

# create 
def  create_agency(data: dict):
    # raise exceptions.AgencyAlreadyExist(f"an agency with the name {data['name']} already exist")
    try:
        AGENCY_COLLECTION.document(data['contact_email']).set(data)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"message": "error creating agency"}
        )
    return data['contact_email']

def create_branch(data: dict):
    pass

# retrive 
def get_agencies():
    docs = AGENCY_COLLECTION.get()

    return [doc.to_dict() for doc in docs]

# update 
def update_agency(data: dict):
    print(data)


def update_branch(data: dict, agency_id: int, branch_id: int):
    print(data)


def update_user(user_id: str, data: dict):
    try:
        db.collection("users").document(user_id).update(data)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"message": "error updating user"}
        )
    


class CreateUser:
    def __init__(self, data: dict) -> None:
        self.data = data
        if not self.data['email'] or not self.data['password']:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    'messsage': 'missing email or password'
                }
            )
        
        self.create_auth()

    def create_auth(self):
        email = self.data['email']
        password = self.data['password']
    

        if self.user_exist:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    'message': 'a user with this email already exist'
                }
            )

        try:
            self.user = auth.create_user(
                email=email,
                password=password
            )
        except:
            raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail={
                'message': 'Could not create user Auth'
            }
        )

        self.add_user_data()

        
        
            
        

    def add_user_data(self):
        try: 
            data = self.data
            del data['password']
            user_id = self.user.uid

            print(data)
            db.collection(USERS_COLLECTION).document(user_id).set(data)
        except:
            # delete user
            auth.delete_user(user_id)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Could not add create data'
            )
        
    @property
    def user_exist(self):
        try:
            auth.get_user_by_email(self.data['email'])
            return True
        except UserNotFoundError:
            return False
         
class USER_FROM_TOKEN:
    def __init__(self, token: dict) -> None:
        self.token = token 
        self.user = self.get_user_from_token()

    @property
    def data(self):
        if self.user:
            ref = db.collection(USERS_COLLECTION).document(self.user['uid']).get()
            if ref.exists:
                data = ref.to_dict()
                data['id'] = self.user['uid']
                return data
        return {}


    def get_user_from_token(self):
        try:
            user = auth.verify_id_token(self.token)
            return user
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    'message': 'invalid token or empty token'
                }
            )
        except InvalidIdTokenError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    'message': 'invalid token'
                }
            )

        except ExpiredIdTokenError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    'message': 'specified ID token has expired'
                }
            )
        except RevokedIdTokenError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    'message': 'the ID token has been revoked'
                }
            )
    
