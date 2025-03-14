# get 2 numbers
# get the numbers between 2 numbers
# print result

# get 2 numbers
print("input two numbers (whole numbers only)")
num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))

# get the numbers between 2 numbers
if num1 < num2 :
    for i in range (num1, num2) :
        print(i)