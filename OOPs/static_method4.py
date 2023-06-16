#calling static method inside a static method

class students:
    @staticmethod
    def mentor(name):
        print(name)

    @staticmethod
    def mentor_age(age):
        print(age)
        students.mentor("Krish")

    @classmethod
    def mentors(cls):
        cls.mentor_age(40)
    #calling static method inside a instance method
    def instance_mentor(self,mentors_list):
        print(mentors_list)
        self.mentor("Ayan")


students.mentors()
students.mentor_age(40)
st1= students()
st1.instance_mentor("Ayan")