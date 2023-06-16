class PartyAnimal:
    x = 0
    def party(self): # self, which refers to the instance of the class on which the method is being called.
        self.x = self.x + 1
        print("So far",self.x)
an = PartyAnimal() # construct object/instance of the class PartyAnimal
an.party() #party method is called
an.party()
an.party()
PartyAnimal.party(an) #call the party method within the 'an' object