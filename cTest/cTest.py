# import the module
from ctypes import c_void_p, c_double, c_int, cdll, addressof
import ctypes
# load the library
lib = cdll.LoadLibrary('../c++/libTestLibrary.so')


class TestObject(object):
    def __init__(self, number):
        self.obj = lib.TestObject_new(c_int(number))


# create a Geek class
class Geek(object):

    # constructor
    def __init__(self):
        # attribute
        self.obj = lib.Geek_new()

    # define method
    def myFunction(self):
        lib.Geek_myFunction(self.obj)

    def testere(self, testObject):
        return lib.Geek_testere(self.obj, testObject.obj)




# create a Geek class object
f = Geek()
testObject = TestObject(5)

# object method calling
f.myFunction()

result = f.testere(testObject)
print(result)
