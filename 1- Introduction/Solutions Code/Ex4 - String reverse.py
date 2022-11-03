#Write a function to reverse a string
def reverse_string1(str):
    str1 = ""   # Declaring empty string to store the reversed string  
    for i in str:  
        str1 = i + str1  # The for loop iterated every element of the given string, join each character in the beginning and store in the str1 variable.
        print(str1)     # Use this print statement to view the details of each iteration
    return str1    # It will return the reverse string to the caller function  
####################
def reverse_string2(str):
    reverse_String = ""  # Empty String  
    count = len(str) # Find length of a string and save in count variable  
    while count > 0:   
        reverse_String += str[ count - 1 ] # save the value of str[count-1] in reverseString /// str[count-1] is the last character of the string
        count = count - 1 # decrement index  
    return reverse_String
####################
def reverse_string3(str):
    return str[::-1]
    '''
    Generally, a slice operator accepts three parameters - start, stop and step. str[start:stop:step]
    We provided the no value to start and end index, which indicates the start index is 0 and the end is n-1 by default. 
    The step size is -1; 
    it means the string continues the traverse from the end and goes to the start position.
    '''
###############
def reverse_string4(str):
     #print(str)
     if len(str) == 0: # Checking the lenght of string  
        return str   
     else:   
        return reverse_string4(str[1:]) + str[0]   #Recall the function inside of itself with new parameter till the condition of len(str) == 0 is met
        '''
        Explanation (our string is abcd) /// first call : bcd and a is stored (since str[1:] will return the string without the element at index 0) len(str) is now 3 
                                             second call : cd and ba is stored  len(str) is now 2 
                                             third call  : d and cba is stored  len(str) is now 1
                                             last call :   empty  and dcba is return since len(str) is 0 now so the condition is met'''
def reverse_string5(str):
# the reverse function doesnt a string directly but returns: a reversed list of items present in a sequence object.
#So to convert it to string we use the join method that transfrom the list into string a join it with an empty string to have our reversed string
    return "".join(reversed(str)) 

##Let's test it
str = "1234abcd"
print("ORIGINAL STRING : "+str)
print("############################################################")
print("METHOD 1 --- USING FOR LOOPS")
print(reverse_string1(str))
print("############################################################")
print("METHOD 2 - USING WHILE LOOP")
print(reverse_string2(str))  
print("############################################################")
print("METHOD 3 - USING SLICERS")
print(reverse_string3(str))  
print("############################################################")
print("METHOD 4 - USING RECURSION") ## Recursion is a function that keeps calling itself until a condition is met
print(reverse_string4(str))
print("############################################################")
print("METHOD 5 - USING Reversed function")
print(reverse_string5(str))