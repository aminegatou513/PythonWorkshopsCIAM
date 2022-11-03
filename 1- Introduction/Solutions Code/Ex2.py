#Write a function to sum all the numbers in a list // Sample input : (8,2,3,0,7) -> Output : 20
#We define a function using the keyword "def" 
def sum_list(our_list):
    #We initialize a counter with 0
    sum = 0
    #We loop through our list and add the value to the sum variable each time
    for number in our_list:
        sum += number ## same thing as sum=sum+number
    #then we return the value 
    return sum

######### let's test it
my_list = [8,2,3,0,7]
#We just call the function and print out the result
print(sum_list(my_list))