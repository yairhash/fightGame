from db.mongo import Db

data=Db()
def win_or_lose(player,opponent,online_user): 
    online_user_wins=online_user.wins  # נדחך לדאטה
    online_user_losts=online_user.losts
    player_wins=player.wins
    player_losts=player.losts
      
    if player.full_life <20 :
        L='you lost'
        losts=player_losts+1
        setattr(player,'losts',losts)
        total_losts=online_user_losts+losts
        setattr(online_user,'losts',total_losts)
        data.update_record(online_user)                                
        return L
    
    elif opponent.full_life <20 :
        W='you won'
        wins=player_wins+1
        setattr(player,'wins',wins)
        total_wins=online_user_wins+wins
        setattr(online_user,'wins',total_wins)
        data.update_record(online_user)                                
        return W
        
     
    
   
    

        