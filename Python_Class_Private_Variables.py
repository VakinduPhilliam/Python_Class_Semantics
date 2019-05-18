# Python Class Private Object Variables
# "Private" instance variables that cannot be accessed except 
# from inside an object don’t exist in Python.
# However, there is a convention that is followed by most Python 
# code: a name prefixed with an underscore (e.g. _spam) should 
# be treated as a non-public part of the API (whether it is 
# a function, a method or a data member). 

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

