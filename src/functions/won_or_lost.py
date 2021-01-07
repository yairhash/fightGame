from db.mongo import Db

def won_or_lost(player,user):
        wins=player.wins
        losts=player.losts
        print(f'your record is {wins} wins and {losts} losts')
        data=Db()
        data.update_record(wins,losts,user)