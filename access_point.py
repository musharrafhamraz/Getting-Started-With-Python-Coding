class Person:
    def __init__(self):
        self.__name = "name"

a = Person()
# Value cannot be accessed
# print(a.__name)

# Value can be accessed
print(a._Person__name)
