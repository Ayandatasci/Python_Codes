class car:
    def __init__(self, year, speed,company):
        self.__year= year
        self.__speed= speed
        self.__company= company
    def get_year(self):
        return self.__year
        
c1= car(2022, 45, "Toyota")

print(c1.get_year())