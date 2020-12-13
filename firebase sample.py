from oauth2client.client import Storage
import pyrebase
from pyrebase.pyrebase import Auth
firebaseConfig = {
    'apiKey': "AIzaSyCkMZu9DYzKwS_8DVdiu4ogI-11PNIO5Jc",
    'authDomain': "python-with-firebase-95dc9.firebaseapp.com",
    'databaseURL': "https://python-with-firebase-95dc9.firebaseio.com",
    'projectId': "python-with-firebase-95dc9",
    'storageBucket': "python-with-firebase-95dc9.appspot.com",
    'messagingSenderId': "720944308267",
    'appId': "1:720944308267:web:3d78a7be15b64bf591ca6e",
    'measurementId': "G-T64D7V28EJ"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()
# storage = firebase.storage()


def login():
    email = "abcd@gmail.com"
    password = "qwerty"
    user = auth.sign_in_with_email_and_password(email, password)
    # print(info)
    # token = user["idToken"]
    info = auth.get_account_info(user['idToken'])
    # print(user)
    # print(info)
    # k = info['users']
    # print(info)
    print(info['users'][0]['emailVerified'])
    # print(type(k))
    # try:
    #     info = auth.sign_in_with_email_and_password(email, password)
    #     # print(info)
    #     print(info.idToken)
    #     print("SIGN_IN_SUCCESSFUL")
    # except:
    #     print("INVALID_TRY_AGAIN")


login()


def signUP(email, password):
    try:  # AIzaSyCkMZu9DYzKwS_8DVdiu4ogI-11PNIO5Jc
        user = auth.create_user_with_email_and_password(email, password)
        token = user["idToken"]
        # print(info)
        print(token)
        auth.send_email_verification(user['idToken'])
        print("SIGN_UP_SUCCESS")
    except:
        print("SIGN_UP_ERROR")


# signUP("anand.shivam44@yahoo.com", "qwerty")


# signUP("efgh@gmail.com","qwerty")
# login()
# info = auth.get_account_info
# print(info.__str__)
# print(auth)


# Storage

def uploadfile():
    try:
        cloudfilename = "test_1.txt"
        storage.child(cloudfilename).put("sample_2.txt")
        print("FILE_UPLOAD_SUCCESS")
    except:
        print("FILE_UPLOAD_FAILURE")


def downloadfile():
    try:
        cloudfilename = "test_1.txt"
        print(storage.child(cloudfilename).get_url(None))
        storage.child(cloudfilename).download()
    except:
        print("FAILURE")


# downloadfile()


def dataBase():
    # data = {"name": "shivam", "age": 21, "employed": False,
    #         "Home": "Deoghar", "College": "BIT Sindri"}
    # try:
    #     db.child("users").child("SHIVAM ANAND").set(data)
    #     print("DATA_PUSH_SUCCESS")
    # except:
    #     print("DATA_PUSH_FAILURE")

    all_users = db.child("users").get()
    for user in all_users.each():
        print(user.key())  # Morty
        print(user.val())  # {name": "Mortimer 'Morty' Smith"}


# dataBase()
