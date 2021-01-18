from flask import Flask , render_template , url_for , redirect , request ,jsonify ,session
app = Flask(__name__)
app.secret_key=b'X\xb8\xf4\x19U;\xaf\x8b\x12\xfcr\xde\x19\x11\x9a\xba'
from db.mongo import Db
from user.user import User
from wepon.wepon import Wepon
from characters.character import Character
from functions.random_opponent import your_random_opponent
from functions.attack import attack
from functions.create_character import create_character
from passlib.hash import pbkdf2_sha256
import uuid

db=Db()
wepon=Wepon()
# player=None
# opponent=None

@app.route("/")
def home():
    return render_template('home.html') 

@app.route("/signup", methods=['POST','GET'])
def signup():
    user=User(uuid.uuid4().hex,request.form['name'],request.form['email'],request.form['password'],0,0)
    if request.method=='POST': 
        insert_status=db.insert_to_db(user)
        if insert_status:
            session['_id']=user._id
            session['name']=user.name
            session['email']=user.email
            session['wins']=user.wins
            session['losts']=user.losts
            session['character']=None
            return redirect(url_for('deshboard'))
        return 'user already exist'
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    _id,name,email,password,wins,losts=db.get_user_from_db(request.form['email'])
    user_from_db=User(_id,name,email,password,wins,losts)
    verify_password=pbkdf2_sha256.verify(request.form['password'],user_from_db.password)
    if request.form['email']==user_from_db.email and verify_password:
        session['_id']=user_from_db._id
        session['name']=user_from_db.name
        session['email']=user_from_db.email
        session['wins']=user_from_db.wins
        session['losts']=user_from_db.losts
        session['character']=None
        global online_user
        online_user=User(user_from_db._id,user_from_db.name,request.form['email'],request.form['password'],user_from_db.wins,user_from_db.losts)
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
    session['character']=request.form['character']
    print(session['character'])
    wepon_obj,shield_obj=wepon.print_wepon_and_shield(session['character'])
    print(wepon_obj,shield_obj)
    
    return render_template('choose_wepon.html',wepon_obj=wepon_obj,shield_obj=shield_obj)

@app.route("/battle_info", methods=['POST','GET'])
def battle_info ():
    wepon_name=request.form['wepon']
    shield_name=request.form['shield']
    global player
    global opponent
    player,opponent=create_character(wepon_name,shield_name,session['character'])
    return render_template('battle_info.html',player=player,opponent=opponent)

@app.route('/battle_results',methods=['POST','GET'])
def battle_results():
    battle_report=attack(player,opponent,online_user)        
    return render_template('battle_info.html',battle_report=battle_report, player=player,opponent=opponent)
    
@app.route('/start_new_game')    
def start_new_game():
    return redirect(url_for('start_game'))

@app.route("/signout")
def signout():
    session.clear()
    return render_template('home.html')


  