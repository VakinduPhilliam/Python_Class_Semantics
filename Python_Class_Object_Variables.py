# Python Class Object Variables
# When a non-data attribute of an instance is referenced, 
# the instance’s class is searched. If the name denotes a valid 
# class attribute that is a function object, a method object is 
# created by packing (pointers to) the instance object and 
# the function object just found together in an abstract object: 
# this is the method object. When the method object is called with 
# an argument list, a new argument list is constructed from the 
# instance object and the argument list, and the function object 
# is called with this new argument list.

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks                # Displays ['roll over']
e.tricks                # Displays ['play dead']
