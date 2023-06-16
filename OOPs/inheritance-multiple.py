class Employee:
    company="Visa"
class Freelancer:
    company="Google"
class Programmer(Employee, Freelancer):
    name="Ayan"
p=Programmer()
print(p.company) # Prints Visa coz in line 5 "Employee" is written first
print(p.name)

