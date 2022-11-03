#In this exercice we need to print the type of elements in a list 
#Means print if this item is an int or string or list or whatever
#Let's take this list of random elements
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12]] #This list containts multipe data types , let's print them
for item in datalist:
    print("Type of ",item," is ",type(item)) # easy just use the predefined type() function to return the type of the element