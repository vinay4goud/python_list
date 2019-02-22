"""
creating a relationship using  data  like father mothe r etc and also creating ralationship with other file data using  moodules

"""


import tempo2

p1 = {1: {'name':'mahankali', 'gender':'male', 'fid':'none','mid':'none','id':1},
           2: {'name':'maha', 'gender':'female', 'fid':'none','mid':'none','id':2},
           3: {'name':'venkat', 'gender':'male', 'fid':1,'mid':2,'id':3},
           4: {'name':'laxman', 'gender':'male', 'fid':1,'mid':2,'id':4},
           5: {'name':'laxmi', 'gender':'female', 'fid':1,'mid':2,'id':5},
           6: {'name':'padma', 'gender':'female', 'fid':'none','mid':'none','id':6},
           7: {'name':'vinay', 'gender':'male', 'fid':3,'mid':6,'id':7},
           8: {'name':'navin', 'gender':'male', 'fid':3,'mid':6,'id':8}

       }
class Me:
    """
    writing a class name called Me
    """

    def __init__(self, uid):
        """
            we are trying  to  call a  id  from here
        :param uid:
        """
        self.id = uid

    def profile(self):

        """
        calling  a perticular  profile based on id we provide
        :return:
        """
        return p1.get(self.id,{})

    def get_name(self):
        """
        here we are  calling the  name of the  person
        :return:
        """
        return self.profile().get('name','NA')

    def father_name(self):
        """
        we are calling father  name of the  person
        :return:
        """

        fid = self.profile().get('fid','na')
        return p1.get(fid,{}).get('name','na')
    def mother_name(self):
        """

        we are  calling mother  name
        :return:
        """

        mid = self.profile().get('mid','na')
        return p1.get(mid,{}).get('name','na')

    def grandfather_name(self):
        """
        calling the grand father name based on the limited information

        """
        fid = self.profile().get('fid','na')
        gf = p1.get(fid,{}).get('fid','na')
        return p1.get(gf,{}).get('name','na')

    def grandmother_name(self):

        """

        calling grand mother name using  the limited information
        :return:
        """

        fid = self.profile().get('fid','na')
        gm = p1.get(fid,{}).get('mid','na')
        return p1.get(gm,{}).get('name','na')

    def brother_name(self):
        """

        calling brother name based  on the father name if of the persond is  equal to fid  the he should be brother of the person uid
        :return:
        """
        fid = self.profile().get('fid','na')

        l =[]
        if fid !='none':
            for i in p1:
                if i != self.id and p1.get(i).get('fid','na') == fid:

                     l . append(p1.get(i).get('name','na'))
            return( f'number of brothers  {len(l)}  they  are {l} ')




    def sister_name(self):
        """
        calling  sister name based on father id
        :return:
        """
        fid = self.profile().get('fid', 'na')
        if fid != 'none':
            for i in p1:
                if i != self.id:
                    if p1.get(i).get('fid', 'na') == fid and p1.get(i).get('gender', 'na')== 'female':

                        return p1.get(i).get('name', 'na')

    def aunt_name(self):

        """

        calling the aunty name based  on  father's father id equal to other person father id and  she must  be female
        :return:
        """

        fid = self.profile().get('fid','na')

        if fid!='none':
            gf = p1.get(fid,{}).get('fid','na')
        else :
            gf ='none'

        if gf!='none':
            for  i in p1:
                if p1.get(i).get('fid','na') == gf and  p1.get(i).get('gender','na')== 'female':



                    return p1.get(i).get('name','na')

    def childrens(self):

        """
        any of the id's fid is equal to passed he becomes father
        :return: childrens
        """

        l = []

        for i in p1:
            if p1.get(i).get('fid', 'na') == self.id:
                l.append(p1.get(i).get('name', 'na'))
        return (f'number of childrens  {len(l)}  they  are {l} ')



    def grand_children(self):
        """
                any of the person son and his son beomes grand son
                :return: childrens
         """

        l = []
        for i in p1:
            if p1.get(i).get('fid', 'none')==self.id:
                for a in p1:
                    if p1.get(a).get('fid', 'none') == i:
                        l.append(p1.get(a).get("name", "na"))
                return(f'grand children {len(l)} they are {l}')

    def uncle(self):
        mid = self.profile().get('mid', 'na')

        k = tempo2.p2.get(mid,{}).get('fid')
        l = []
        for i in tempo2.p2:
            if  tempo2.p2.get(i).get('fid') == k and tempo2.p2.get(i).get('gender','na')== 'male':
                l.append(tempo2.p2.get(i).get("name"))
        return(f'uncle  {len(l)} they are {l}')

        #if mid!='none':
         #   gf = tempo2.p2.get(mid,{}).get('fid','na')
        #else :
         #   gf ='none'

        #if gf!='none':
         #   for  i in tempo2.p2:
          #      if tempo2.p2.get(i).get('fid','na') == gf and  tempo2.p2.get(i).get('gender','na')== 'male':
#
 #                   return tempo2.p2.get(i).get('name','na')

    def brother_inlaw(self):
        """
         persons mothers brother(uncle) son  called as brother in law
        first call mother id and her fid
        second compair above fid  with other person who has it
        third if above fid is equal  call the id who met with mothers fid
        with the help of id call person name who has it as fid
        :return:
        """
        mid = self.profile().get('mid', 'na')

        k = tempo2.p2.get(mid, {}).get('fid')
        l = []
        for i in tempo2.p2:
            if tempo2.p2.get(i,{}).get('fid','na') == k:
                biw = tempo2.p2.get(i,{}).get('id')
                for e in tempo2.p2:
                    if tempo2.p2.get(e,{}).get('fid') == biw:

                        return tempo2.p2.get(e,{}).get('name','na')

















obj = Me(5)
name = obj.get_name()
father = obj.father_name()
mother = obj.mother_name()
grandfather = obj.grandfather_name()
grandmother = obj.grandmother_name()
brother = obj.brother_name()
sister = obj.sister_name()
aunt = obj.aunt_name()
childrens = obj.childrens()
grand_children = obj.grand_children()
uncle = obj.uncle()
brother_inlaw =obj.brother_inlaw()

print(f'name : {name}')
print (f'father : {father}')
print (f'mother : {mother}')
print (f'grand  father : {grandfather}')
print (f'grand  mother : {grandmother}')
print (f'brother : {brother}  ')
print (f'sister : {sister}')
print (f'aunt : {aunt}')
print (f'childrens : {childrens}')
print (f'grand childrens :{grand_children}')
print (f'uncle : {uncle}')
print (f'brother_inlaw : {brother_inlaw}')










'''
def a(n):

    y=1

    while y<10:
        b = p1.get(y).get('name')
        print(b)
        if n==b:
            print(b)
            break
        y+=1
a('mahankali')

'''