# Python Class Object Instantiation _init( )_
# Python Class objects support two kinds of operations: 
# 1. Attribute references. 
# 2. Instantiation.
# More details on Python Class Instantiation.
# The instantiation operation (“calling” a class object) creates an empty object. 
# Many classes like to create objects with instances customized to a specific 
# initial state. 
# Therefore a class may define a special method named __init__(), like this:

 def __init__(self):
    self.data = []

# When a class defines an __init__() method, class instantiation automatically 
# invokes __init__() for the newly-created class instance. 
# So in this example, a new, initialized instance can be obtained by:

x = MyClass()

# Of course, the __init__() method may have arguments for greater flexibility. 
# In that case, arguments given to the class instantiation operator are passed 
# on to __init__(). 
