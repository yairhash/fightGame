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
from functions.win_or_lose import win_or_lose
from passlib.hash import pbkdf2_sha256
import uuid

db=Db()
wepon=Wepon()

@app.route("/")
def home():
    return render_template('signup.html') 

@app.route("/signup", methods=['POST','GET'])
def signup():
    new_user=User(uuid.uuid4().hex,request.form['name'],request.form['email'],request.form['password'],0,0)
    if request.method=='POST': 
        insert_status=db.insert_to_db(new_user)
        if insert_status:
            return  redirect('login_page')
        return 'user already exist'
    return render_template('signup.html')

@app.route("/login_page")
def login_page():
    return render_template('login.html') 

@app.route('/login', methods=['POST'])
def login():
    _id,name,email,password,wins,losts=db.get_user_from_db(request.form['email'])
    user_from_db=User(_id,name,email,password,wins,losts)
    verify_password=pbkdf2_sha256.verify(request.form['password'],user_from_db.password)
    if request.form['email']==user_from_db.email and verify_password:
        session['email']=user_from_db.email   
        global online_user
        online_user=User(user_from_db._id,user_from_db.name,request.form['email'],request.form['password'],user_from_db.wins,user_from_db.losts)
        return redirect(url_for('dashboard'))
    return 'wrong password/name combination'    
        
@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        return render_template('dashboard.html',online_user=online_user)
    return 'something went wrong'

@app.route("/start_game")
def start_game():
    return render_template('choose_character.html')

@app.route("/choose_character", methods=['POST','GET'])
def choose_character():
    session['character']=request.form['character']
    wepon_obj,shield_obj=wepon.print_wepon_and_shield( session['character'])
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
    battle_report=attack(player,opponent)  
    battle_results=win_or_lose(player,opponent,online_user)    
    return render_template('battle_info.html',battle_report=battle_report ,battle_results=battle_results, player=player,opponent=opponent)

@app.route('/start_new_game')    
def start_new_game():
    return redirect(url_for('start_game'))

@app.route("/signout")
def signout():
    session.clear()
    return render_template('signup.html')


@app.route('/top_5',methods=['POST','GET'])
def top_5():
    top_5=db.get_top_five()
    return render_template('dashboard.html', top_5=top_5 ,online_user=online_user)
        

@app.route('/my_ranking',methods=['POST','GET'])
def my_ranking():
    my_ranking=db.get_my_ranking(online_user)
    return render_template('dashboard.html',my_ranking=my_ranking ,online_user=online_user)  