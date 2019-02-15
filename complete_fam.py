class family:

    def __init__(self, name, gender, fid, mid,nid):
        self.name = name
        self.gender = gender
        self.fid = fid
        self.mid = mid
        self.nid = nid
    
    def a(self):
        self.name =c
        c = p1.get(8).get('name')
        
        print ('names'+ self.name)

p1 = { 8: {'name':'mahankali', 'gender':'male', 'fid':'none','mid':'none','id':8},
           9: {'name':'maha', 'gender':'female', 'fid':'none','mid':'none','id':9},
           1: {'name':'venkat', 'gender':'male', 'fid':8,'mid':9,'id':1},
           10: {'name':'laxman', 'gender':'male', 'fid':8,'mid':9,'id':10},
           11: {'name':'laxmi', 'gender':'female', 'fid':8,'mid':9,'id':11},
           2: {'name':'padma', 'gender':'female', 'fid':6,'mid':7,'id':2},
           3: {'name':'vinay', 'gender':'male', 'fid':1,'mid':2,'id':3},
           4: {'name':'navin', 'gender':'male', 'fid':1,'mid':2,'id':4}
       }
b = family(p1)
b.a()


#print (c.get('name'))
