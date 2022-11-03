#Let's count even and odd numbers from a series of numbers
#Even = pair // Odd = impair
#We initialize two counters 
pair = 0
impair = 0 
my_numbers = [2,5,8,9,6,4,5,6,4,2,4,9,20,15,899,45158,1286,12368,13,45,3,35,40]
#Loop through my list of numbers
for number in my_numbers:
    if number%2==0 : # % means the rest of the division for exemple 5%2 = 1 // 4%2 = 0 ..
        pair += 1
    else:
        impair += 1
print(pair,impair)
#####################WE CAN ALSO USE THE random library to generate a list of numbers randomly !
from random import randint #We imported the randint function wish returns only INTEGERS RANDOMLY IN A GIVEN RANGE
#Initialize empty list 
my_random_list = []
#Let's say I want to generate 100 random number and those numbers must be between 0 and 80
for i in range(100):
    my_random_list.append(randint(0,80))
print(my_random_list)
