## Animal is-a object
class Animal(object):
    pass

## Dog is-a Animal and has-a __init__ which takes self and name as parameters
class Dog(Animal):

    def __init__(self, name):
        ## Dog instance has-a name
        self.name = name

## Cat is-a Animal and has-a __init__ which takes self and name as parameters
class Cat(Animal):

    def __init__ (self, name):
        ## Cat instance has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__ (self, name):
        ## Person instance has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__ (self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Person instance has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
