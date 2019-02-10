class family:
    def __init__(self, gp):

        self.gp = gp
 #       self.p = p
 #       self.c = c

gp = { 'grand_parent' : ['mahankali', 'narsamma'],
       'mahankali_sons' : (' venkat', ' laxman'),
       'children_of_venkat' : ('vinay', 'naveen')
       }

mahankali = { 'name' : ' mahankali',
              'age' : 70,
              'geder' : 'male',
              'father' : 'abhayya',
              'aunt' : 'na',
              'sibilings' : '2 of them rajayya and anjayya',
              'nephews' : '1 and his name is stya',
              'no. of childrens': 4
              }
h = list(mahankali.keys())
u = list(mahankali.values())

grany = family(gp)

x =  ( grany.gp.get('grand_parent' ))

print( " name of the person is ' mahankali'")

y = { 'a' : [input(" enter name : ")],
      'b' : [if h[1] == input("age : "):
                 print (i[1])]
            }
z= y.get('a')

if x[0]==z[0]:
       print( mahankali.get('name'))
       
