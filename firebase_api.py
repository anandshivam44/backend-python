import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import pyrebase
from pyrebase.pyrebase import Auth

app = FastAPI(debug=True)


class AuthInfo(BaseModel):
    email: str
    password: str

    # signUp: bool = Falseimport uvicorn


app = FastAPI(debug=True)


firebaseConfig = {
    'apiKey': "AIzaSyCkMZu9DYzKwS_8DVdiu4ogI-11PNIO5Jc",
    'authDomain': "python-with-firebase-95dc9.firebaseapp.com",
    'databaseURL': "https://python-with-firebase-95dc9.firebaseio.com",
    'projectId': "python-with-firebase-95dc9",
    'storageBucket': "python-with-firebase-95dc9.appspot.com",
    'messagingSenderId': "720944308267",
    'appId': "1:720944308267:web:3d78a7be15b64bf591ca6e",
    'measurementId': "G-T64D7V28EJ"
}#paste config files here
firebase = pyrebase.initialize_app(firebaseConfig)
# db = firebase.database()
auth = firebase.auth()
# storage = firebase.storage()


@app.get("/")
async def home():
    return {"Home": "API working"}


@app.post("/auth/signup/")
async def signUP(authInfo: AuthInfo):
    try:
        user = auth.create_user_with_email_and_password(
            authInfo.email, authInfo.password)
        token = user["idToken"]
        # print(token)
        auth.send_email_verification(user['idToken'])
        print("SIGN_UP_SUCCESS")
        return user
    except:
        return {"Status": "Sign Up Error"}


@app.post("/auth/login/")
async def login(authInfo: AuthInfo):
    try:
        user = auth.sign_in_with_email_and_password(
            authInfo.email, authInfo.password)
        info = auth.get_account_info(user['idToken'])
        # print(info['users'][0]['emailVerified'])
        if info['users'][0]['emailVerified'] == 0:
            return "EMAIL_NOT_VERIFIED"
        return user
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        # return message
        return message


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
