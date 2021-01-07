from flask import Flask
from app import app
#from models import User


# user=User()

@app.route("/user/signup", methods=['POST'])
def signup_form():
    #return user.sign_up()


@app.route("/user/sigout")
def signout():
    return user.sign_out()
    
   
