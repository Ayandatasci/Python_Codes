class car:
    def __init__(self,company,price,mileage):
        self.company= company
        self.price= price
        self.mileage= mileage
    def get_info(self):
        print(f"The company of the car is {self.company}")
        print(f"The price of the car is ${self.price}")
        print(f"The mileage of the car is {self.mileage}km")

car1= car("Maruti",70000,23)
car1.get_info()
print()
car2= car("Hyundai",80000,19)
car2.get_info()
print(car1.price)