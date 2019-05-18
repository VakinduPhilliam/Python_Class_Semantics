# Python Class Iterators
# Having seen the mechanics behind the iterator protocol, 
# it is easy to add iterator behavior to your classes. 
# Define an __iter__() method which returns an object 
# with a __next__() method. 
# If the class defines __next__(), then __iter__() can 
# just return self:
 
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
