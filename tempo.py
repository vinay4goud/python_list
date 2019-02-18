


p2 = [1, 2, 3, 4, 5, 6, 8, 9]
p3 = ['name', 'gender', 'fid', 'mid', 'nid']
p4 = 'none'
p5 = dict.fromkeys(p3,p4)
#print(p5)
p6 = dict.fromkeys(p2,p5)
#print (p6)
p7=['vinay',' navin', 'venkat', 'padma', 'laxman', 'laxmi', 'mahankali', 'maha']
p8=[]
y = input('enter id : ')

p6 = dict.fromkeys(p2,p5)
p6 [int(y)]['name']=p7[(int(y)-1)]

if  int(y)==3 or int(y)==4 or int(y)==5 or int(y)==6:
    p6 [int[y]]['gender'] = ['female']

if int(y) <= 10:

    print(p6.get(int(y)))
#else :
   # print ('none')



#print(p5)




p1 = {8: {'name':'mahankali', 'gender':'male', 'fid':'none','mid':'none','id':8},
           9: {'name':'maha', 'gender':'female', 'fid':'none','mid':'none','id':9},
           1: {'name':'venkat', 'gender':'male', 'fid':8,'mid':9,'id':1},
           6: {'name':'laxman', 'gender':'male', 'fid':8,'mid':9,'id':6},
           5: {'name':'laxmi', 'gender':'female', 'fid':8,'mid':9,'id':5},
           2: {'name':'padma', 'gender':'female', 'fid':10,'mid':11,'id':2},
           3: {'name':'vinay', 'gender':'male', 'fid':1,'mid':2,'id':3},
           4: {'name':'navin', 'gender':'male', 'fid':1,'mid':2,'id':4}

       }

'''
x = ['key1', 'key2', 'key3']
y = [1,2,3]
z = [4,5,6]
abc =dict.fromkeys(y,z)
print(abc)
thisdict = dict.fromkeys(x, abc)

print(thisdict)


c = p1.get(1)
print (c)


for w,x in p1.items():

    print(x)

    for z,y in x.items():
        print (y)


'''


#a = {[8]:[1]}
#a[8]=1
print
'''
i = 0
while i<12:
    j = p1.get(i).get('fid')
    if j== u:
         break
         print(j)
    i += 1

'''
'''
#i = 1

for i in p1:
    if p1.get(int(i)).get('fid') == 8 and p1.get(int(i)).get('gender') == 'female':
     '''   # print(i) '''

        #print (x)'''

'''
while i <12:
    #w = p1.get(int(i)).get('fid')
    if p1.get(int(i)).get('fid')==8 and p1.get(int(i)).get('gender')== 'female':

        print(i)

    i += 1
'''

