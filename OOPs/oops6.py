class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def info(self):
        print(f"\nThe name of the train is {self.name}")
        print(f"The fare is {self.fare}")
        print(f"The seats available are {self.seats}")
    def booktickets(self):
        if (self.seats>0):
            print(f"Your ticket has been booked & seat number is {self.seats}\n")
            self.seats=self.seats-1
        else:
            print("Sorry this train is full, kindly try tatkal\n")

a=Train("Rajdhani Express","₹1500",2)
a.info()
a.booktickets()
a.booktickets()
a.booktickets()