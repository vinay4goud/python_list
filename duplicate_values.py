
"""
printing the duplicate values 
"""
my_list = [20,30,20,30,40,50,15,11,20,40,50,15,6,7]

"""
sorting the given list for comparing with result
""" 
my_list.sort()
print(my_list)
 
new_list = sorted(set(my_list))
dup_list =[]
 
 """
 here  wwe need to count the each value which is greaer and 1
 if the value is greater than 1 it is a duplicate value and it should be added to empty list which we can call it later 
 """
for i in range(len(new_list)):
        if (my_list.count(new_list[i]) > 1 ):
            dup_list.append(new_list[i])
        
print(dup_list) 


"""
based on the aboce program below program written to fins the duplicate strings 
similar fashion of code written using strings  
"""

name = ['vinay', 'vinay', 'navin', ' kumar']

name.sort()
print(name)
name_sort = sorted (set(name))
dup_name = []

for x in range (len(name_sort)):
    if ( name.count(name_sort[x])>1):
        dup_name.append(name_sort[x])

print(dup_name)



