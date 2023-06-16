class Employee:
    company="Google"
    salary=1000
Ayan=Employee() #Object instantiation
Ankita=Employee()
print(Ayan.company)
print(Ankita.company)
print()#new line
Employee.company="Microsoft" #changing class attribute
print(Ayan.company)
print(Ankita.company)

Ayan.salary=900
Ankita.salary=950
print(Ayan.salary)
print(Ankita.salary)