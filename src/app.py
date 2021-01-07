from flask import Flask , render_template , url_for , redirect , request ,jsonify ,session
from pymongo import MongoClient
from user import models
from passlib.hash import pbkdf2_sha256
from user.models import User
from functions.your_choise import your_choise
import uuid
import pymongo 
app = Flask(__name__)
app.secret_key=b'\xc6\x18\xf3P1\xab\xef+\xef\xae\x98\xcc\xc2W\x0b\xd0'
cluster=MongoClient('mongodb+srv://root:root@cluster0.ykasy.mongodb.net/test')
db=cluster['user']
collection=db['info']
user=User()

  
@app.route("/")
def home():
    return render_template('home.html') 


@app.route("/signup", methods=['POST','GET'])
def signup():
    user={
        '_id':uuid.uuid4().hex,
        'name':request.form['name'],
        'email':request.form['email'],
        'password':request.form['password']   
    }
    if request.method=='POST':
        existing_user=collection.find_one({'email':user['email']})
        if existing_user is None:
            password_encrypted=pbkdf2_sha256.encrypt(user['password'])
            collection.insert_one({'_id':user['_id'],'name':user['name'] ,'email':user['email'],'password':password_encrypted})
            session['_id']=user['_id']
            session['name']=user['name']
            session['email']=user['email']
            return redirect(url_for('deshboard'))
        return 'user already exist'
    
    return render_template('home.html')


@app.route('/login', methods=['POST'])
def login():
    user_info=request.form.to_dict()
    inserted_email=user_info['email']
    user_in_db=collection.find_one({{'email':inserted_email}})
    user_encrypted_password=user_in_db['password']
    user_online_password=request.form['password']
    verify_password=pbkdf2_sha256.verify(user_online_password,user_encrypted_password)
    if user and verify_password:
        session['_id']=user_in_db['_id']
        session['name']=user_in_db['name']
        session['email']=user_in_db['email']
        return redirect(url_for('deshboard'))
    
    return 'wrong password/name combination'    
        
                        
@app.route('/deshboard')
def deshboard():
    if 'name' in session:
        return render_template('dashboard.html')
    return 'something went wrong'


@app.route("/start_game")
def start_game():
    return render_template('start_game.html')


@app.route("/choose_character", methods=['POST','GET'])
def choose_character ():
    char_type=str(request.form['character'])
    player,opponent=your_choise(char_type)
    return render_template('battle_info.html',player=player,opponant=opponent)


@app.route("/signout")
def signout():
    session.clear()
    return render_template('home.html')

  