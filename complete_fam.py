''' 

Find solutions for folloing problem statement using class, List, Dict, tuples and sets.


 1. what is the name of the person ?
 

2. is the person is male or female ?


 3. what is their father name ?


 4. what is his/her grandfather name (paternal/maternal) ?


 5. what is his/her aunt name ? 


 6. how many number of siblings are there and name them ?
 

7. how many number of nephews and name them ?
 

8. how many children does your grandfather has and name them ?


 9. Information of the particular person

'''



class family:

    def __init__(self, nid):
        
        self.nid = nid




    
    def a(self):



        if self.nid == y:
            print('name id : ' + self.nid)
            x = p1.get(int(y)).get('fid')    #  father details fetch
            z = p1.get(int(y)).get('mid')    # mother details fetch
            u = p1.get(int(x)).get('fid')         # grand father
            v = p1.get(int(x)).get('mid')       # grand mother
            '''   
             father's father  id is equal to any of the female father id then she is aunty
             '''
            #if p1.get(11).get('fid') == u:
             #   w=p1.get(11).get('name')
            if x == 'none' or z == 'none':
                x = 'none'
                z = 'none'
            elif x == p1.get(int(y)).get('fid') and z == p1.get(int(y)).get('mid') :
                x= p1.get(int(y)).get('fid')
                z= p1.get(int(y)).get('mid')



            if u == 'none' or v == 'none':
                u = 'none'
                v = 'none'
            elif u == p1.get(int(x)).get('fid') and v == p1.get(int(x)).get('mid'):
                u= p1.get(int(x)).get('fid')
                v= p1.get(int(x)).get('mid')

            for i in p1:
                if p1.get(i).get('fid') == u and p1.get(i).get('gender') == 'female':
                    break



            #i = 1
            #while i<12:
             #   if p1.get(i).get('fid') == u and p1.get(i).get('gender') == 'female':
              #      #print(i)
               #     break
                #else :
                 #   i = 'no aunt'

              #  i += 1



                #print('yes')

            print ( 'name : ' + p1. get ( int ( y ) ) . get( 'name' ) +
                   '\ngender : ' + p1.get(int(y)).get('gender') +
                   '\nfather : ' + p1.get(int(x)).get('name') +                 #father
                   '\nmother : ' + p1.get(int(z)).get('name')  +               # mother

                   '\ngrand father : ' + p1.get(int(u)).get('name') +           # grand father
                    '\ngrand  mother : ' + p1.get(int(v)).get('name')        # grand  mother
                    )
            print(
                    ' \naunt : ' + p1.get(int(i)).get('name')                   # aunty

               )
        else :
            print(' enter valid id ')


p1 = {8: {'name':'mahankali', 'gender':'male', 'fid':'none','mid':'none','id':8},
           9: {'name':'maha', 'gender':'female', 'fid':'none','mid':'none','id':9},
           1: {'name':'venkat', 'gender':'male', 'fid':8,'mid':9,'id':1},
           6: {'name':'laxman', 'gender':'male', 'fid':8,'mid':9,'id':6},
           5: {'name':'laxmi', 'gender':'female', 'fid':8,'mid':9,'id':5},
           2: {'name':'padma', 'gender':'female', 'fid':'none','mid':'none','id':2},
           3: {'name':'vinay', 'gender':'male', 'fid':1,'mid':2,'id':3},
           4: {'name':'navin', 'gender':'male', 'fid':1,'mid':2,'id':4}
       }

y= input('enter id : ')

b = family(y)
b.a()

'''
if  x == 8:
    print  ( p1.get(y).get('name'))
y = int(input('enter id : '))


b = family (p1.get(y).get('name'),

            p1.get(y).get('gender'),

            str(p1.get(y).get('fid')),

            str(p1.get(y).get('mid')),

            str(p1.get(y).get('id')))


b.a()
'''
