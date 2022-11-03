'''
Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1.
'''
## Image presentation and explication => https://www.w3resource.com/w3r_images/python-conditional-image-exercise-11.png
row_num = int(input("Input number of rows: "))        
col_num = int(input("Input number of columns: "))
#NOTICE HERE WE used int before input , since input function returns what you wrote as a string then int convert it to an actual number
#### A TWO DIMENSIONAL ARRAY IS ACTUALLY JUST A LIST INSIDE A LIST 
# this a list [5,8,9] it's elements are just ints , this a 2D-List [[5,8,9],[4,5,8]] its elements are actually lists (I will a document with more examples for this kind of lists)
list1 = []
list2 = []
for i in range(row_num):
    #We iterate over the numbers of row we inputed
    #and in each row we iterate over the columns (basically like a matrix)
    for j in range(col_num):
        list2.append(i*j) #we append the value i*j in the list for all columns ex : [x,y,z] // [a,b,c]
    list1.append(list2) # then we append the list containing the columns values into our row list [[x,y,z],[a,b,c]]
    list2=[] # each time we clear column list to calculate the new values and append it
print(list1) 
print("##########################################################################")
print("METHOD 2")
multi_list = [[0 for col in range(col_num)] for row in range(row_num)] # Initialise an empty 2D Array with 0's [[0,0,0],[0,0,0] etccc ]
print(multi_list)

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col #Update the value with row*col 
print(multi_list)



