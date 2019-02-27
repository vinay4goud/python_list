"""
JSON is a syntax for storing and exchanging data.

it has methods to convert sting format file data type as  well as data type to string format


"""

import json # importing json

d = '{"a":"vinay", "b":40}'  # string value
e = {"a": "navin", "c":45}   # data type value

class j_son:
    # b = '{"a":"vinay", "b":40}'

    """
    calling the value
    """
    def __init__(self, a):
        self.a = a

        # self.y = y

    def load_(self):

        '''
        writing function to convert string to data type
        :return: data type value
        '''
        #z = self.a
        h = json.loads(self.a)
        f = json.loads(self.a)
        #print(h)
        return h
    def dump_(self):
        """
        writing function to convert data type value to  string value
        :return: sring value 
        """

        h = json.dumps(self.a)
        return(h)


z = j_son(d)
zz = j_son(e)
print (z.load_())

print (zz.dump_())
#print(j_son)

# zz = z._loads()

# a = {"a":"vinay", "b": 40}
#print(f'{json.dumps(a)}')


# print (z)
