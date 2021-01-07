from flask import Flask , jsonify , request , session , redirect
import uuid
from passlib.hash import pbkdf2_sha256
import pymongo
from pymongo import MongoClient
cluster=MongoClient('mongodb+srv://root:root@cluster0.ykasy.mongodb.net/test')
db=cluster['user']
collection=db['info']

        
class User():
    
    def start_session(self,user):
        del user['password']
        session['logged_in']=True 
        session['user']=user
        return jsonify(user),200

    def sign_up(self):
        #getting user data from the browser
        user={ 
            "_id":uuid.uuid4().hex,
            "name":request.form.get['name'],
            "email":request.form.get['email'],
            "password":request.form.get['password']
        }
    
        #encrypt password
        user['password']=pbkdf2_sha256.encrypt(user['password'])
        #check for existing email address
        if collection.find_one({'email':user['email']}):
            return jsonify({'error':'email address already in use'})
        
        user=collection.insert_one(user)
        if user.acknowledged==True:
            return self.start_session(user)     
        else:
            return False
        
            
    def sign_out(self):
        session.clear()
        return redirect('/') 
    
    def login(self):
        data_from_user=request.form.get('email')
        user=collection.find_one({{'email':data_from_user}})
        if user:
            return self.start_session(user)               
        else:
            return jsonify({'error':'something went wrong'})
