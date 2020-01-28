class Test:
    
    name = 'I am the class'
    variable = 10

    def printName(self, age):
        print('I am a method of the class')
        print(age)


x = Test()
# print(x.name)


class Test2:

    def __init__(self, name):
        self.name = name
        print('I am the init function')

# y = Test2('y')
# print(y.name)
# x = Test2('x')
# print(x.name)


class Dog:

    scientific_name = 'Canis'

    def __init__(self, name):
        self.name = name

duke = Dog('duke')
bob = Dog('bob')

# print(duke.scientific_name)
# print(duke.name)

# print(bob.scientific_name)
# print(bob.name)


class Hero:

    def __init__(self, name):
        self.name = name
        self.energy = 100
    
    def eating(self, food):
        if food == 'pasta':
            self.energy = self.energy + 10
        elif food == 'pizza':
            self.energy = self.energy - 20

mario = Hero('Mario')
# print(mario.name)
# print(mario.energy)
# mario.eating('pasta')
# print(mario.energy)
# mario.eating('pizza')
# print(mario.energy)


# adissu = Hero('Adissu')
# print(adissu.name)
# adissu.eating('pasta')
# print(adissu.energy)

# for i in range(0, 4):
#     mario.eating('pizza')

# print(mario.energy)


class BaseClass:

    def printName(self):
        print('I come from the Base Class')

class SubClass(BaseClass):
    
    def printName(self):
        print('I come from the Sub Class')

a = SubClass()
a.printName()








class Employee:

    def __init__(self, name, paycheck):
        self.name = name
        self.paycheck = paycheck
    
    def raise_paycheck(self, number):

        self.paycheck = self.paycheck + (self.paycheck * number)

mario = Employee('Mario', 1000)
print(mario.name)
print(mario.paycheck)

mario.raise_paycheck(0.1)
print(mario.paycheck)








