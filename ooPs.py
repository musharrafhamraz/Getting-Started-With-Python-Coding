# class Tree:
#     def __init__(self, name, height) -> None:
#         self.name = name
#         self.height = height

#     def show(self):
#         print(f'The name of tree is {self.name} with a height of {self.height}M')

# a = Tree('Almond', 5)

# a.show()

class Person:
    def __init__(self, name, age, number):
        self.name = name
        self.age= age
        self.number = number

    def show(self):
        print(f'The name of the Person is {self.name} his age is {self.age} and his number is {self.number}')

person1 = Person("Musharraf", 22, "+923466497023")

Person.show(person1)

class Man(Person):
    def __init__(self):
        pass
    
