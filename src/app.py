from flask import Flask , render_template , url_for , redirect , request ,jsonify ,session
from pymongo import MongoClient
from passlib.hash import pbkdf2_sha256
from functions.your_choise import your_choise
from characters.character import Character
from functions.random_opponent import your_random_opponent
from functions.attack import attack
import uuid
import pymongo 
from db.mongo import Db
from user.user import User
from wepon.wepon import Wepon
from functions.attack import attack
app = Flask(__name__)
app.secret_key=b'\xc6\x18\xf3P1\xab\xef+\xef\xae\x98\xcc\xc2W\x0b\xd0'
cluster=MongoClient('mongodb+srv://root:root@cluster0.ykasy.mongodb.net/test')
db=cluster['user']
collection=db['info']


  
@app.route("/")
def home():
    return render_template('home.html') 


@app.route("/signup", methods=['POST','GET'])
def signup():
    user=User(uuid.uuid4().hex,request.form['name'],request.form['email'],request.form['password'])
    if request.method=='POST':
        existing_user=collection.find_one({'email':user.email})
        if existing_user is None:
            password_encrypted=pbkdf2_sha256.encrypt(user.password)
            collection.insert_one({'_id':user._id,'name':user.name ,'email':user.email,'password':password_encrypted})
            session['_id']=user._id
            session['name']=user.name
            session['email']=user.email
            return redirect(url_for('deshboard'))
        return 'user already exist'
    
    return render_template('home.html')


@app.route('/login', methods=['POST'])
def login():
    user=User(None,None,request.form['email'],request.form['password'])
    db=Db()
    _id,name,email,password=db.get_user(user.email)
    user_from_db=User(_id,name,email,password)
    verify_password=pbkdf2_sha256.verify(user.password,user_from_db.password)
    print(verify_password)
    if user.email==user_from_db.email and verify_password:
        session['_id']=user_from_db._id
        session['name']=user_from_db.name
        session['email']=user_from_db.email
        return redirect(url_for('deshboard'))
    
    return 'wrong password/name combination'    

@app.route("/start_game")
def start_game():
    return render_template('choose_character.html')
        
@app.route('/deshboard')
def deshboard():
    if 'name' in session:
        return render_template('dashboard.html')
    return 'something went wrong'


@app.route("/choose_character", methods=['POST','GET'])
def choose_character():
    global char_type
    char_type=request.form['character']
    wepon_obj,shield_obj=your_choise(char_type)
    return render_template('choose_wepon.html',wepon_obj=wepon_obj,shield_obj=shield_obj)


@app.route("/battle_info", methods=['POST','GET'])
def battle_info ():
    wepon_name=request.form['wepon']
    shield_name=request.form['shield']
    wepon_class=Wepon()
    wepon_power=wepon_class.get_wepon_value(wepon_name)
    shield_power=wepon_class.get_shield_value(shield_name)
    global player
    player=Character(char_type,250,wepon_name,wepon_power,shield_name,shield_power)
    random_opp=your_random_opponent(char_type)
    global opponent
    opponent=Character(random_opp.char_type,random_opp.full_life,random_opp.wepon_name,random_opp.wepon_power,random_opp.shield_name,random_opp.shield_power)
    return render_template('battle_info.html',player=player,opponent=opponent)
    
    
@app.route('/battle_results',methods=['POST','GET'])
def battle_results():
    result=attack(player,opponent)
    return render_template('battle_info.html',result=result, player=player,opponent=opponent)
    
    
        
@app.route("/signout")
def signout():
    session.clear()
    return render_template('home.html')


  