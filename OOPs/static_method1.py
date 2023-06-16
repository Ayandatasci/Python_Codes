#calling static method inside a class method

class employee:
    @staticmethod
    def company():
        print("Company is Google")

    @classmethod
    def salary(cls):
        print("Salary is $50k")
        cls.company() #calling static method

employee.salary() #calling class method