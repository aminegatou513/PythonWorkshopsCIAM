def sumofnumbers(list):
    sum =0
    for num in list:
        sum+=num
    return sum

def average(list):
    return sumofnumbers(list)/len(list)


number = 1
list_of_numbers= []
while number!=0:
    number=int(input("Enter a number--- Enter 0 to stop "))
    if number == 0:
        break
    else:
        list_of_numbers.append(number)
print("Numbers entered are :",end="")
print(list_of_numbers)
print("Sum of numbers entered is : "+str(sumofnumbers(list_of_numbers)))
print("Average of numbers entered is : "+str(average(list_of_numbers)))

######### Method 2
print("Method 2 without functions")
count = 0
sum = 0.0
number = 1

while number != 0:
	number = int(input("Enter a number--- Enter 0 to stop"))
	sum = sum + number
	count += 1

if count == 0:
	print("Input some numbers")
else:
	print("Average and Sum of the above numbers are: ", sum / (count-1), sum)


