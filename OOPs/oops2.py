class Employee:
    company="Google"
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender= gender
        print("\nEmployee is created") #constructor is a special method which runs as soon as the object is created.
    def getinfo(self):
        print(f"The name of the employee is {self.name}")
        print(f"The age of the employee is {self.age}")
        print(f"The gender of the employee is {self.gender}")
    def getsalary(self,sign):
        print(f"Salary is 180k\n{sign}")
    def phn_no(self):
        print(f"Phone Number is {self.phn} and his company is {self.company}")
    @staticmethod #Sometimes we need a function that doesn’t use the self-parameter.
    def greet():
        print("Good Morning, Sir\n")
Ayan=Employee("Ayan",18,"Male") #object is created
Ayan.getsalary("Thanks")
Ayan.phn= 9123027681
Ayan.phn_no()
Ayan.getinfo()
Ayan.greet()