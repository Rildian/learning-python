list1 = [1, 2, 3, 4]
list2 = [9, 83, 1, 3]

num1 = set(list1)
num2 = set(list2)

# some operators w/ set
# | union operator (its not union all)
print(num1 | num2)

# diff, it removes the inserction
print(num1 - num2) # after removing the intersection, it shows the unique values on the 1st set
print(num2 - num1) # in this case, it'll show unique values of the num2

# symmetric dif
print(num1 ^ num2) # it'll show unique values of both, values that arent on the intersection

# and - inserction
print(num1 & num2) # the common of both sets (like inner join in sql)

num1.add(69)
print(num1)
num1.add(1)
print(num1) # even though i've added, it doesnt show.


num1.update([34984398, 19289, 2398, 'm']) # its not a list that was added, it was single elements, like append simultaneoosly
print(num1)

lista69 = []
lista69.append([2983923832, 2093328, 238239823]) # the values added is a list
print(lista69)

num1.discard(30) # i can use this, even though i dont have any 30 
#num1.remove(30) # => now i cant do that

# remember the introduction of sets? see
s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 1}
s3 = s1.union(s2)
print(s3)

s3 = s1.difference(s2)
print(s3)



