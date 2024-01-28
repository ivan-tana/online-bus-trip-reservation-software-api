import pyrebase

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


firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()