class students:
    def __init__(self,name,email):
        self.name= name
        self.email= email
    @classmethod #it overloads init
    def details(tap,name,email): #by class method
        return tap(name, email)
    
    def student_details(self,name,email): #normal
        return(self.name, self.email)
    
test= students.details("Ayan", "ayan@gmail.com") # calling without creating object
print(test.name)
print(test.student_details("Ankita","ankita@gmail.com"))

#del students.details #deletes details()
#test= students.details("Ayan", "ayan@gmail.com")

delattr(students,"student_details")
print(test.student_details("Ankita","ankita@gmail.com"))