import json

d = '{"a":"vinay", "b":40}'
e = {"a": "navin", "c":45}

class j_son:
    b = '{"a":"vinay", "b":40}'

    def __init__(self, a):
        self.a = a

        # self.y = y

    def load_(self):
        #z = self.a
        h = json.loads(self.a)
        f = json.loads(self.a)
        #print(h)
        return h
    def dump_(self):
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
