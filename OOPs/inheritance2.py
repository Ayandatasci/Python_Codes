class class1:
    def test_class1(self):
        print("Method of class 1")
class class2(class1):
    def test_class2(self):
        print("Method of class 2")
class class3(class2):
    pass
obj= class3() #object of class3()
obj.test_class1()
obj.test_class2()