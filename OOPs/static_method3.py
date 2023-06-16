#calling static method inside a static method

class universe:
    @staticmethod
    def static1():
        print("This is static method 1")

    @staticmethod
    def static2():
        print("This is static method 2")
        universe.static1() #calling static1

universe.static2() #calling static2
