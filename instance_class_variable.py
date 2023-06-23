# Instance variable are associated with intance not with class 

class Person:
    # Class variable applies to every object of the class
    companyName = 'Microsoft'
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
    def show(self):
        print(f'The name of the Person is {self.name} his raise amount is {self.raise_amount} and the company name is {self.companyName} ')

person1 = Person("Musharraf")
# Instance variable only applies to the specific object of the class
person1.raise_amount= 0.3
# we can also change class variable for a specific object of the class
person1.companyName = "Microsoft-Mine"
person2 = Person("Hamraz")

Person.show(person1)
Person.show(person2)