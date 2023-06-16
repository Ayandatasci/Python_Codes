class students:
    def __init__(self,name,email):
        self.name= name
        self.email= email
    @classmethod
    def details(tap,name,email):
        return tap(name, email)
    
    def student_details(self,name,email):
        return(self.name, self.email)
    
test= students.details("Ayan", "ayan@gmail.com")
print(test.name)
print(test.student_details("Ankita","ankita@gmail.com"))
#Class is logical abstraction because it provides a logical structure for all of its objects. It gives an overview of the features of an object