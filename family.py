


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
venkat = { 'name' : ' venkat',
              'age' : 50,
              'geder' : 'male',
              'father' : 'mahankali',
              'aunt' : 'na',
              'sibilings' : '1 and his name is laxman',
              'nephews' : 'NA',
              'no. of childrens': 2
              }
vinay =     { 'name' : ' vinay',
              'age' : 26,
              'geder' : 'male',
              'father' : 'venkat',
              'aunt' : 'laxmi',
              'sibilings' : '1 and his name is navin',
              'nephews' : 'NA',
              'no. of childrens': 'NA'
              }
naveen =  { 'name' : ' naveen',
              'age' : 24,
              'geder' : 'male',
              'father' : 'venkat',
              'aunt' : 'laxmi',
              'sibilings' : '1 and his name is vinay',
              'nephews' : 'NA',
              'no. of childrens': 'NA'
              }
laxman = { 'name' : ' laxman',
              'age' : 45,
              'geder' : 'male',
              'father' : 'mahankali',
              'aunt' : 'na',
              'sibilings' : '1 and his name is venkat',
              'nephews' : 'NA',
              'no. of childrens': 2
              }





grany = family(gp)
x = ( grany.gp.get('grand_parent'))
a = (grany.gp.get('mahankali_sons'))
e = ( grany.gp.get('children_of_venkat'))

for ab in x:
    print ( " grand parents  names : " + ab )

for bc in  a :
    print (" parents names : " + bc )
    
for cd in  e:
    print (" childrens names : " +cd)
    
y = input("please enter the ' name from above mentioned'   : ")            

if x[0] == y:
    print ('head of the family tree : ' +'"'+ x[0] + '"') 
elif x[1] ==y:
    print ('"'+ x[0] + '"'+' sibiling name  is :' +'"' +x[1]+ '"')
    
if  y =="sibiling" or y == "brother"  :

   z =  input (" please enter if required parents as'p' or grnad parents as 'gp' : ")
   if z == "p":
         print(f"elder one is {a[0]} and the  younger one is  {a[1]} both of them are sons of {x[0]}")
                
        
   elif z =="gp":
        print ( f"elder one is {x[0]} and the younger one is {x[1]} ")

if y == "father" or y== " nanna":
    
    relat = input(" please enter if required parents as'p' or grnad parents as 'gp' : " )
    if relat == "p":
        print(f" parents of the both he sibilings {a[0]} and {a[1]} is {x[0]}")

    elif relat == "gp":
        print(f" parents of the both he sibilings {x[0]} and {x[1]} is abhayya" )

if  y == 'vinay' :
   
    for f,k in vinay.items():
         print(f+"      :  ",k)

elif y == 'naveen':
    for l,m in naveen.items():
        print (l+"      :  ",m)
        
elif y == 'mahankali':
    for d,e in mahankali.items():
        print (d+"      :  ",e)
elif y == 'venkat':
    for e,f in venkat.items():
        print(e+"      :  ",f)
elif y == 'laxman':
    for f,g in laxman.items():
        print(f +"      :  ", g)



  
            
        
        
