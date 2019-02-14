family = { 8: {'name':'mahankali', 'gender':'male', 'fid':'none','mid':'none','id':8},
           9: {'name':'maha', 'gender':'female', 'fid':'none','mid':'none','id':9},
           1: {'name':'venkat', 'gender':'male', 'fid':8,'mid':9,'id':1},
           10: {'name':'laxman', 'gender':'male', 'fid':8,'mid':9,'id':10},
           11: {'name':'laxmi', 'gender':'female', 'fid':8,'mid':9,'id':11},
           2: {'name':'padma', 'gender':'female', 'fid':6,'mid':7,'id':2},
           3: {'name':'vinay', 'gender':'male', 'fid':1,'mid':2,'id':3},
           4: {'name':'navin', 'gender':'male', 'fid':1,'mid':2,'id':4}
           }
a= { 'a':'b',  #'''sample variable'''
     'v':'c'
     }
d={'m':a,   # ''''smple variable''''
   'n':'m'
   }
#print(d)



y= int(input("enter id : "))

v =family.get(y)

a = list(family)

'''
b = family.get(2)
c = family.get(3)
d = family.get(4)
e = family.get(5)
f = family.get(6)
h = family.get(7)
i = family.get(8)
j = family.get(9)
k = family.get(10)'''

print (v)


# v['id']=family.get(y).get('name')
#''' reference  one helpful'''

'''#for l, x in v.items():'''
if  y == a[0]:
        b =list(v.values())

        c =list(v.keys())

        print (f'name is {b[0]}')
        print (f'gender is {b[1]}')
        print (f'father is {b[2]}')
        print (f'mother is {b[2]}')
        if v['id']== family.get(1).get('fid') :#and  v[id]==family.get(10).get('fid'):
            print (f'son is {family.get(1).get("name")}') 
        
        
elif y==a[1]:
        b =list(v.values())

        c =list(v.keys())

        print (f'name is {b[0]}')
        print (f'gender is {b[1]}')
        print (f'father is {b[2]}')
        print (f'mother is {b[2]}')
        if v['id']== family.get(1).get('fid') :#and  v[id]==family.get(10).get('fid'):
            print (f'son is {family.get(1).get("name")}') 
        
         
elif y==a[2]:
        b =list(v.values())

        c =list(v.keys())

        print (f'name is {b[0]}')
        print (f'gender is {b[1]}')
        print (f'father is {family.get(8).get("name")}')
        print (f'mother is {family.get(9).get("name")}')
        if v['id']== family.get(3).get('fid') :#and  v[id]==family.get(10).get('fid'):
            print (f'son is {family.get(3).get("name")}') 
        
         
elif y==a[3]:
         print(l + ' : ',x )
         
elif y==a[4]:
         print(l + ' : ',x )
         
elif y==a[5]:
         print(l + ' : ',x )
         
elif y==a[6]:
         print(l + ' : ',x )
         
elif y==a[7]:
         print(l + ' : ',x )

#if y == a[0]: ''' #  reads id  :8 values '''
