'''
In python , we can easily show a string multiple times in one line by multiplying it
for exemple
str = "test"
print(str*5) => will print "testtesttesttesttest"
Starting from this logic we will solve this exercice to print
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''
#As you can see, each line contains a number and that number is how many times that number will repeat 1 will repeat 1 time / 2 - two times..... / 9 - 9 times
for i in range(1,10): #10 to include 9
    print(str(i)*i) #str(i) transform the number to string and mutlipying it by itself (number version) so that it will be repeated that many times
