'''vinay = [ 'name','father','mother']
vinay[0]=['vinay']
vinay[1]=['venkat']
vinay[2]=['padma']

#mahankali = ['mahankali', 

#def a(name,father,mother):'''
    
'''
a1 = ['venkat' , 'mahankali','maha']
a2 = ['padma','venkata','shanti']
a3 = ['vinay',a1[0], a2[0]]
a4 = ['navin',a1[0],a2[0]]

print('name'= a4[0], 'father'= a4[1], 'mother'=a4[2])
'''
''' data as been inserted in the name family '''

family = { 8: {'name':'mahankali', 'gender':'male', 'fid':'none','mid':'none','id':8},
           9: {'name':'maha', 'gender':'female', 'fid':'none','mid':'none'},
           1: {'name':'venkat', 'gender':'male', 'fid':8,'mid':9},
           10: {'name':'laxman', 'gender':'male', 'fid':8,'mid':9},
           11: {'name':'laxmi', 'gender':'female', 'fid':8,'mid':9},
           2: {'name':'padma', 'gender':'female', 'fid':6,'mid':7},
           3: {'name':'vinay', 'gender':'male', 'fid':1,'mid':2},
           4: {'name':'navin', 'gender':'male', 'fid':1,'mid':2}
           }
a= { 'a':'b',  '''sample variable'''
     'v':'c'
     }
d={'m':a,     '''smple variable'''
   'n':'m'
   }
#print(d)
print(family.get(1))  '''exicuting the value '''

'''  above value is not reading  'fid': 8 '''

           
