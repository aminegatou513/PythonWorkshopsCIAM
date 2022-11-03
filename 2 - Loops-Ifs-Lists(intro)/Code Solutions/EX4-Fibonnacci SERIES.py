#I'm supposing you already know what's fibonnacci series right? Ensam students should know :p
#Since we want the fibo series beetween 0 and 50
#The first two numbers are always 0,1 
# SO 
x,y = 0,1
while y<50:  # While we didn't reach 50 we do our calculations
    print(y) #Print our fibo number
    x,y=y,y+x # Then we increment our counters x will take y , and y will take x+y :) That's fibonnaci :p

