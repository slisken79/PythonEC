CITY_OF_ORIGIN = "Uppsala"


class Person():
    def __init__(self, age=10, name="John"):
        super().__init__()
        self.__age = age
        self.name = name
        self.__city = CITY_OF_ORIGIN

    def get_person_age(self):
        """Gets the age of the person"""
        return self.__age

    def print_person_age(self):
        print(self.__age)
