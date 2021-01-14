import pymongo
from pymongo import MongoClient
cluster=MongoClient('mongodb+srv://root:root@cluster0.ykasy.mongodb.net/test')
db=cluster['user']
collection=db['info']


class Db(): 
    
    def get_user(self,email):
        user=collection.find_one({'email':email}) 
        print(user)
        if user:
            return user['_id'],user['name'],user['email'],user['password']
        else:
            return False
       
            
            
            
    # def insert_to_db(self,user_info,):
    #     db_user=collection.insert_one(user_info)
    #     {print('data inserted')if db_user.acknowledged==True else print('somthing went wrong')}
    #     _id=db_user.inserted_id               
    #     return _id
                
    # def update_record(self,win,lost,user):    # update user's record
    #     user_id=user.user_name
    #     update=collection.update_one({'id':user_id},{'$set':{'wins':win}},{'$set':{'losts':lost}})        
    #     print('the data was updated')if update.acknowledged==True else print('sonthing went wrong')
     
    # def validate_log_in(self,user_name,password):
    #     # verify_password=   
    #     user=collection.find_one({'user_name':user_name})
    #     if user==True and user['pssword']==password:   
    #         print('You are connected') 
    #         return user
    #     else:
    #         print('something went wrong,try again')   
    #     return False               
    
   
        
        
                  
            
            
           
            
        
               
       
 
        
             
        
        
              
                