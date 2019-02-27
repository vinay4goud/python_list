"""
JSON is a syntax for exchanging data.

it has methods to convert sting to data  as  well as data  to string


"""

import json  # importing json

# string
d = '{"a":"vinay", "b":40}'

# dictionary
e = {"a": "navin", "c": 45}


class Json:
    # b = '{"a":"vinay", "b":40}'

    def __init__(self, a):
        """
           taking value
            """
        self.a = a

        # self.y = y

    def loads(self):
        """
          convert string to data
        :return: data , json value
        """
        # z = self.a
        h = json.loads(self.a)
        # f = json.loads(self.a)
        # print(h)
        return h

    def dump_(self):
        """
        convert data to string, json value
        :return: string, json value
        """

        h = json.dumps(self.a)
        return h

u = type(e)
z = Json(d)
zz = Json(e)

k = z.loads()
print(f'reads complete value of file {k}')
print(f'reads  sing value of file : {k["a"]}')

p = zz.dump_()
print(f'reading  complete value of the file {p}')


#q = zz.loads()

#print(q,'none')

if u == str:
    print(f'{zz.loads()}')
else:
    print('wrong data  entered')




# print (f'reading  single value  of file {p}')

# zz = z._loads()

# a = {"a":"vinay", "b": 40}
# print(f'{json.dumps(a)}')


# print (z)
