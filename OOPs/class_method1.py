class customer:
    mobile=912789635
    def __init__(self,name,age,city):
        self.name= name
        self.age= age
        self.city= city

    @classmethod
    def change_mobile(tap, mobile):
        customer.mobile= mobile

    @classmethod
    def details(ok, name, age, city):
        return ok(name,age,city)
    
    def customer_details(self):
        return self.name,self.age,self.city,customer.mobile
    
def state(cls, state_name):
    print(state_name)
customer.state= classmethod(state)
customer.state("WB")
    
test= customer.details("Sam",19,"Kolkata")
print(test.name)
print(test.age)
print(test.city)
print(test.mobile) # prints initial value
test.change_mobile(923455123)
print(test.mobile) # prints changed mobile no
 
print(test.customer_details())