import pymongo
from pymongo import MongoClient
cluster=MongoClient('mongodb+srv://root:root@cluster0.ykasy.mongodb.net/test')
db=cluster['user']
collection=db['info']
from passlib.hash import pbkdf2_sha256

class Db(): 
    def insert_to_db(self,user):
        existing_user=collection.find_one({'email':user.email})
        if existing_user is None:
            password_encrypted=pbkdf2_sha256.encrypt(user.password)
            collection.insert_one({'_id':user._id,'name':user.name ,'email':user.email,'password':password_encrypted,'wins':0,'losts':0})
            return True
        return False
    
    def get_user_from_db(self,email):
        user=collection.find_one({'email':email}) 
        if user:
            return user['_id'],user['name'],user['email'],user['password'],user['wins'],user['losts']
        return False
    
    def update_record(self,online_user):
        user=collection.find_one({'_id':online_user._id})
        if user:
            myquery = { "_id":online_user._id}
            newvalues = { "$set": { "wins":online_user.wins}}
            newvalues1 = { "$set": { "losts":online_user.losts}}
            collection.update_one(myquery,newvalues)
            collection.update_one(myquery,newvalues1)
        return 'something went wrong'
          
    def get_top_five(self):
        position=1
        li=[]
        users=collection.find().sort('wins',-1).limit(5)
        for doc in users:
            li.append((position,doc['name'],doc['wins']))
            position=position+1
        return li
     
    def get_my_ranking(self,online_user):
        position=1
        li=[]
        users=collection.find().sort('wins',-1)
        for doc in users:
            if online_user.email==doc['email']:
                li.append((position,doc['name'],doc['wins']))
            else:
                position=position+1
        return li
                
                 
           
            
        
               
       
 
        
             
        
        
