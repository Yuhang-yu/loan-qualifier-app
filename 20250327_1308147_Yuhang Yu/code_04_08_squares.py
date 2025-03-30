# In this script, you will print out table with a seuncial numbers and correspounding squares numbers

#Print the table heading
print("Number\tSquare")
print("-------------")
#print number 1 through 10 and their squares
for num in range(1,1001):
    square = num ** 2
    print(num,'\t', square)