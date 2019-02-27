"""
JSON is a syntax for storing and exchanging data.

it has methods to convert sting format file data type as  well as data type to string format


"""

import json  # importing json

d = '{"a":"vinay", "b":40}'  # string value
e = {"a": "navin", "c": 45}  # data type value


class Json:
    # b = '{"a":"vinay", "b":40}'

    """
    calling the value
    """

    def __init__(self, a):
        self.a = a

        # self.y = y

    def loads(self):
        """
        writing function to convert string to data type
        :return: data type value
        """
        # z = self.a
        h = json.loads(self.a)
        f = json.loads(self.a)
        # print(h)
        return h

    def dump_(self):
        """
        writing function to convert data type value to  string value
        :return: string 
        """

        h = json.dumps(self.a)
        return h


z = Json(d)
zz = Json(e)

k = z.loads()
print(f'reads complete value of file {k}')
print(f'reads  sing value of file : {k["a"]}')

p = zz.dump_()
print(f'reading  complete value of the file {p}')
# print (f'reading  single value  of file {p}')

# zz = z._loads()

# a = {"a":"vinay", "b": 40}
# print(f'{json.dumps(a)}')


# print (z)
