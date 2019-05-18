# Python Function Outside Class
# It is not necessary that the function definition is textually 
# enclosed in the class definition: assigning a function object 
# to a local variable in the class is also ok. For example:
# Function defined outside the class.

def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
