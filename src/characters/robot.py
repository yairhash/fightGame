class Robot():
    
    def __init__(self,name,wepon_name,wepon_power,full_life,char_type):
        self.name = name
        self.wepon_name=wepon_name
        self.wepon_power=wepon_power
        self.full_life = full_life
        self.char_type=char_type
        
    def get_type(self):
        return self.char_type 