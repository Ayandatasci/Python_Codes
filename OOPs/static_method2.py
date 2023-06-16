#calling static method inside a class method
class students:
    @staticmethod
    def mentor(mentor_list):
        print(mentor_list)

    @classmethod
    def mentor_name(cls):
        cls.mentor(["ram","raman"])

students.mentor_name()