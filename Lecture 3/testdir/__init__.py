print("JAG BEFINNER MIG I PYTEST3!")


class Person():
    def __init__(self, age=10, name="John"):
        super().__init__()
        self.age = age
        self.name = name

    def get_person_name(self):
        pass


my_person = Person(age=12, name="Rose")
print(dir(my_person))
print("my persons age is: ", my_person.age)
print("my persons name is: ", my_person.name)
