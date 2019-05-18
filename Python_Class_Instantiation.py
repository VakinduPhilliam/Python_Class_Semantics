# Python Class Object Instantiation
# Python Class objects support two kinds of operations: 
# 1. Attribute references. 
# 2. Instantiation.
# This example expands on Instantiation

class Complex:
     def __init__(self, realpart, imagpart):
         self.r = realpart
         self.i = imagpart

 x = Complex(3.0, -4.5)
 x.r, x.i                 # Displays (3.0, -4.5)
