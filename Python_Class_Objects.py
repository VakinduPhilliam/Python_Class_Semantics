# Python Class Objects
# Python Class objects support two kinds of operations: 
# 1. Attribute references. 
# 2. Instantiation.
# Attribute references use the standard syntax used for all attribute references in Python: obj.name. 
# For Example;

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

# For the above, MyClass.i and MyClass.f are valid attribute references, 
# returning an integer and a function object, respectively.
# On the other hand, Class instantiation uses function notation. 
# Just pretend that the class object is a parameterless function that 
# returns a new instance of the class. 
# For example:

x = MyClass()

# This creates a new instance of the class and assigns this object 
# to the local variable x.
