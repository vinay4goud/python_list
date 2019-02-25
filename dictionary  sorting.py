"""
main moto to sort the data using  dictionaries  
"""
student = {         # dictionary

    'name': [ 'vinay', 'navin', 'uday'],
    'age' : [20, 19, 30]
    }

a = student['name']  # calling the pirticualr key value from above dictionary
c = int (input(' enter value : ')) # manual input


if c<=2 :
    b =  a[c]
    print (b)
else :
    print (" not a valid number  ")

"""
assigning dictionary name values to x and then it is sorted 
"""
x = student['name']
x.sort()


"""
assigning dictionary name values to y and then it is sorted 
"""

y=student['age']
y.sort()

print ( " sort of the name  and age values")
print (x,y)


while y==20:
    print ( count.y)
    y+=1



