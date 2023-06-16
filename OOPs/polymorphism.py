#Polymorphism is a concept in object-oriented programming where an object can take on multiple forms or have multiple behaviors based on its context. 
# I am me but I my behaviour is different when i am in home , when in an interview, when in office i.e, my behaviour chnages depending on the situation or if i say DATA INPUT
class data_sci:
    def syllabus(self):
        print("This is my Data Science syllabus")
class web_dev:
    def syllabus(self):
        print("This is my web development syllabus")

def class_poly(obj):
    for i in obj:
        i.syllabus() #same context but multiple behaviour
obj=[data_sci(), web_dev()] #creates object of the class
(class_poly(obj))