class Programmer:
    company = "Microsoft"
    def __init__(self,name,product,age,exper):
        self.name = name
        self.product = product
        self.age = age
        self.exper = exper
    def getinfo(self):
        print(f"The name of the employee is {self.name}")
        print(f"The product of the employee is {self.product}")
        print(f"The age of the employee is {self.age}")
        print(f"The experience of the employee is {self.exper}\n")

Ayan = Programmer("Ayan","Twitter",19,"5 years")
Ankita = Programmer("Ankita","GitHub",18,"6 years")
Ayan.getinfo()
Ankita.getinfo()
