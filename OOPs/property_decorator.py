class Employee:
    def __init__(self,company,age):
        self.__company= company #privates the company name
        self.age= age

    @property #(GETTER) shows the company name
    def company_name(self):
        return self.__company
    
    @company_name.setter #(SETTER) sets new value
    def company_name_set(self, name):
        self.__company = name

    @company_name.deleter
    def delete_company(self):
        del self.__company #deletes the private variable __company
    
em= Employee("Google",20)
print(em.company_name) #access the company name
em.company_name_set = "Microsoft"
print(em.company_name_set) #prints changed comapny name

del em.company_name #deletes the company_name attribute from the em object
print(em.company_name) 