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
              'childrens': 4
              }
h = list(mahankali.keys())
u = list(mahankali.values())

grany = family(gp)

x =  ( grany.gp.get('grand_parent' ))

#print( " name of the person is ' mahankali'")
# a = if h[1] == input("age : "):    print (u[1])
y =  input(" please enter name : ")
#z= y.get('a')

if x[0]==y :
       print('name  of the person : ' + mahankali.get('name'))
       
       j=( input("what would you like to know  more  about mahankali please mention : "))
       
       if j=='age':
           print (f'{j} of the {y} is {u[1]}')
       elif j =='geder':
           print (f'{j} of the {y} is {u[2]}')
       elif j =='father':
           print (f'{j} of the {y} is {u[3]}')
       elif j =='aunt':
           print (f'{j} of the {y} is {u[4]}')
       elif j =='sibilings':
           print (f'{j} of the {y} is {u[5]}')
       elif j =='nephews':
           print (f'{j} of the {y} is {u[6]}')
       elif j =='childrens':
           print (f'{j} of the {y} is {u[7]}')
       elif j== 'na' or j== 'NA':
           print ( "thank you")

else :
    print  ( "enter some value")
           
