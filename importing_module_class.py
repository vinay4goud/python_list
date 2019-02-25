"""
importing other file program  in this program to acess the data from other file 
"""

import mymodule
class  instance:
    def __init__(self, age):
        self.age = age
age = mymodule.person["b"]
p2 = instance (age)

print (p2.age)
