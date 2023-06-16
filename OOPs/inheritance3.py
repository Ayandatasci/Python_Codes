class papa:
    def papa_msg(self):
        print("Hi, this is Dad")
class mom:
    def mom_msg(self):
        print("Hi, this is Mom")
class child(papa, mom):
    pass

obj=child() # created object of child()
obj.papa_msg()
obj.mom_msg()