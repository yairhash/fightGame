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
            collection.update_one({'id':online_user._id} ,{'$set':{'wins':online_user.wins}},{'$set':{'losts':online_user.losts}})
        return 'something went wrong'

    
    
    

            
            
           
            
        
               
       
 
        
             
        
        
              
                