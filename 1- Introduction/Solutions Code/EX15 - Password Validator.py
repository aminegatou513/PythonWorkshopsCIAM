import string #We imported string module to get access to the alphabets/numbers/symbols directly from the ASCII Table 

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
print(lower+"//"+upper+"//"+numbers+"//"+symbols) #Execute this print statement to view 
## Or you can just use a manual list containing all symbols/numbers ....


while True:
    length_validity=False
    l,u,n,s=0,0,0,0
    p= input("Input your password\n")
    if  5 < len(p) < 17:
        length_validity=True
    for i in p : ###Check if the password contains lower/upper/symbols/numbers and count them
        if i in list(lower):
            l+=1
        if i in list(upper):
            u+=1
        if i in list(numbers):
            n+=1
        if i in list(symbols):
            s+=1
    #############
    if (l>=1 and u>=1 and s>=1 and n>=1 and l+s+u+n==len(p)):
        print("Valid password : "+str(p))  
        break
    if l<1:
        print("You need one lowerCase !")
    if u<1:
        print("You need one UpperCase !")
    if s<1:
        print("You need one Symbol !")
    if n<1 : 
        print("You need one number")
    if length_validity == False:
        print("Length must be between 6 and 16 characters")


