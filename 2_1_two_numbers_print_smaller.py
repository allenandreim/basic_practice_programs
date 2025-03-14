# get two numbers
# check which is smaller
# print result

# get two numbers
num1 = float(input("1st number: "))
num2 = float(input("2nd number: "))
 
# check which is smaller
if num1 > num2 :
    print(num2,"is smaller.")
elif num2 > num1 :
    print(num1,"is smaller.")
else:
    print("numbers are equal.")