from db.mongo import Db
from users.user import User



def log_in():
    user_name =input("Enter user name:")
    password =(input("Enter password:"))
    data=Db()
    user=data.validate_log_in(user_name,password)
    if user==False:
        log_in()
    else:    
        return user
 

 
        
    
        
    
    
    
   
        
            
        
