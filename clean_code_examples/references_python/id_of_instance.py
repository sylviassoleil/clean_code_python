# chain of reference
a = [1]
b = a
id(a) == id(b)
b = ['4']  # or a = ['4']
id(a) == id(b)  # False

''' pointer to the object '''
a = [1]
b = a
id(a) == id(b) #140394455700864
del a
id(b) #140394455700864

''' Python counts the references to an object, if zero references, the object will be collected'''
a = []
a.append(a)
id(a) == id(a[0]) #

''' creation & assignment '''
x = [[0] for _ in range(5)]
x.append(1) #[[0, 1], [0], [0], [0], [0]]
x_append = [[0]] * 5
x_append[0].append(1) # [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]

''' shallow copy v.s. deep copy'''
import copy
x = [[1,2], [3], 5]
y = copy.copy(x) # shallow copy
x[-1] = 1 # y[-1]=5, bcs the value is reassigned


''' largest integer with same id '''
a = 256
b = 256
id(a) == id(b) # True

a = 257
b = 257
id(a) == id(b) # False






