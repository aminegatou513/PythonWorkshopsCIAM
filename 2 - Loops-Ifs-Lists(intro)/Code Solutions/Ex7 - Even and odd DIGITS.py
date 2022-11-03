#Find numbers beetween 100 to 400 (both included) with only even digits
# 100 to 199 will be eliminated because 1 is not even
# 300 to 399 will be eliminated because 3 is not even
# 200 to 299 : eliminate every number who have a odd digit ( 201 - 203 -.....)
winning_numbers = []
for numbers in range(100,401): # we wrote 401 because we want 400 included
    #Transform our number to str so that we can treat each digit as a character
    s = str(numbers)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):   #s[0] is the first digit // s[1] is the second .. 
        #then each digit is transformed to int again so that we can test if it's even or not 
        #This condition will only be true if the 3 nested conditions are true (TRUE AND TRUE AND TRUE = TRUE) classic maths
        winning_numbers.append(s)
    
#Print them in a comma-separated sequence.
print(",".join(winning_numbers))
#The join function will transform the list into a string and join it with the comma 

