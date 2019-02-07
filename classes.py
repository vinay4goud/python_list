class  school_students:
    student = {

    'name': [ 'vinay', 'navin', 'uday'],
    'age' : [20, 19, 30]
    }

x = school_students()
print(x.student['name'])






class  stud:
    def __init__(self, school ):
        self.school = school
        #self.age = age
school = [ 'name', 'age']


p1 = stud (school)



print (p1.school)





class  instance:
    def __init__(self, age):
        self.age = age
age = {

    "name" : [ 'vinay',  'navin',  'kumar'],
    "b" : [ 20, 19, 18]
    }

p2 = instance (age)

print (p2.age.get("b"))


    
