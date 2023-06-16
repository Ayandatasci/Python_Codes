#Write a class calculator capable of finding square, cube, and the square root of a number.
class Caculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f"\nThe square of {self.num} is {self.num**2}")
    def cube(self):
        print(f"The cube of {self.num} is {self.num**3}")
    def square_root(self):
        print(f"The square root of {self.num} is {self.num**0.5}\n")
a=Caculator(9)
a.square()
a.cube()
a.square_root()
