import pyrebase
from firebase_admin import firestore
import datetime
import firebase_admin
from firebase_admin import credentials
import os


firebaseConfig = {
  "apiKey": "AIzaSyA-7GN04OwrefNm6zR3bKtw6vwaetwpzSA",
  "authDomain": "bus-reservation-46c9d.firebaseapp.com",
  "projectId": "bus-reservation-46c9d",
  "storageBucket": "bus-reservation-46c9d.appspot.com",
  "messagingSenderId": "588555460302",
  "appId": "1:588555460302:web:e36f3f94085f7b4d057a9f",
  "measurementId": "G-RXQ6S3GFN1",
  "databaseURL": "https://bus-reservation-46c9d.firebasedatabase.app"
}

cred = credentials.Certificate(os.environ['GOOGLE_APPLICATION_CREDENTIALS']) 
firebase_admin.initialize_app(credential=cred)

firebase = pyrebase.initialize_app(firebaseConfig)
db = firestore.client()

# data = {
#     "stringExample": "Hello, World!",
#     "booleanExample": True,
#     "numberExample": 3.14159265,
#     "dateExample": datetime.datetime.now(tz=datetime.timezone.utc),
#     "arrayExample": [5, True, "hello"],
#     "nullExample": None,
#     "objectExample": {"a": 5, "b": True},
# }

# db.collection("data").document("one").set(data)