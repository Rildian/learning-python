s = "     banana      "
s2 = 'banana'
print(s)
print(s.strip()) # removed the blank spaces
print(s.strip().strip("an")) # removes 
print(s2.split('n')) # removes the n and picks the element before and after the encounter of some n
s3 = 'Rildian'
print(s3.split('l')) 
# if the first letter is the one which is gonna be splited
print(s3.split('R')) # it creates ['', 'ildian'] interesting

print(s3.replace('l', 'u'))

print('Space1 \nSpace2 \nSpace3')
print('Table1\tTable2\tTable3')

s4 = 'How can i use \'quotes\'?' #strange lol
print(s4)

s5 = "Name:\t\'Mr N\'\nAge:\t\'69\'\nCountry:\t\'Nigeria\'\n"
print(s5)
#unicodes
s6 = '\u2764' # a example of unicode
print(s6)
print('\U0001F600') # unicode
