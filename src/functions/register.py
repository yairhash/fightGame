
# from users.user import User
# from .login import log_in
# from db.mongo import Db
# from passlib.hash import pbkdf2_sha256
# import uuid



# #getting the data from the user
# def register():
#         full_name = input("Enter your full name:")
#         user_name = input("Enter user name:")
#         user_age = int(input("Enter age:"))
#         user_country = input("Enter country:")
#         user_password =input("Enter password:")
#         pass_check = input("Enter password agin:")
#         {print("Password match") if user_password == pass_check else print("passwords don\'t match")}
#         user_email = input("Enter email:")
        
#         #ccrete a user obj
#         _id=uuid.uuid4().hex
#         user_info={
#                 '_id':_id,
#                 'full_name':full_name,
#                 'user_name':user_name,
#                 'age':user_age,
#                 'counrty':user_country,
#                 'password':user_password,
#                 'email':user_email,
#                 'wins':0,
#                 'losts':0
#         }
        
#         #encrypt password with passlib
#         user_info['password']=pbkdf2_sha256.encrypt(user_info['password'])
        
        
#         #chaks if user exist in db
#         data=Db()
#         is_user_name_exist=data.check_if_exist(user_info)
#         if is_user_name_exist:
#                 data.insert_to_db(user_info)
#                 user=User(_id,full_name,user_name,user_age,user_country,user_password,user_email,0,0)
#                 log_in()
#                 return user       
#         else:
#                 register()               
               
        
              
    


    
    
    
    
    
    
    
#    ############### just in case################# 
#     #     # login()
#     #     # player,opponent=your_choise()
#     #     # the_great_battle(player,opponent)  
#     # else:
#     #     login()
#     #     
#     #     the_great_battle(player,opponent)    

