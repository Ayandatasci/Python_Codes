#Abstraction is the process of hiding the implementation details of a complex object or system, so that users only need to know how to interact with it.
# Data abstraction is nothing but the combination of abstract class and interface
import abc
class ayan:
    @abc.abstractmethod
    def bike_choice(self):
        pass

    @abc.abstractmethod
    def car_choice(self):
        pass

    @abc.abstractmethod
    def pc_choice(self):
        pass

class age_15(ayan):
    def bike_choice(self):
        return "Super Bikes"
    def car_choice(self):
        return "Racing Cars"
    def pc_choice(self):
        return "Gaming PC"
    
class age_25(ayan):
    def bike_choice(self):
        return "Classical Bikes"
    def car_choice(self):
        return "Family Cars"
    def pc_choice(self):
        return "Work related PC"
    
ayan15=age_15()
print(ayan15.car_choice())
ayan25=age_25()
print(ayan25.bike_choice())