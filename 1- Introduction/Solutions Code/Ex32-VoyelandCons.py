import string
listofalphabets = list(string.ascii_lowercase)
print(listofalphabets)
voyels = ['a', 'e', 'i', 'o', 'u']
for v in voyels:
    listofalphabets.remove(v) # we removed all voyels from the list of alphabets so that we have only cons

l = input("Input a letter")
if l in voyels:
    print(l+" is a voyel")
elif l in listofalphabets:
    print(l+" is a const")
else :
    print(l+" is something else")

