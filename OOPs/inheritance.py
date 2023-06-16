#inheritance is a mechanism where a class can inherit attributes and methods from another class. It allows for code reuse, promotes modularity, and facilitates the creation of hierarchical relationships between classes.
class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")
    
class Programmer(Employee):
    lang="python"

    def getLang(self):
        print(f"The language is {self.lang}")

    def showDetails(self):
        print("This is a programmer")

a=Employee()
b=Programmer()
a.showDetails()
b.getLang()
b.showDetails()