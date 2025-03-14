# get 2 numbers
# get the numbers between 2 numbers
# print result

# get 2 numbers
print("input two numbers (whole numbers only)")
num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))

# get the numbers between 2 numbers
if num1 < num2 : 
    for i in range (num1 + 1, num2) :
        print(i)

elif num1 > num2 :
    for i in range (num2 + 1, num1) :
        print (i)

else : 
    print("numbers are equal and has no other numbers in between.")