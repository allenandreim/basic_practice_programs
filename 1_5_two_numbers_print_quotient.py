# get 2 numbers
# divide num1 to num2
# restrict 0 in divisor 
# print result 

# get 2 numbers
num1 = float(input("1st number(dividend): "))
num2 = float(input("2nd number(divisor): "))

# divide num1 to num2
quotient = num1 / num2

# restrict 0 in divisor 
if num2 != 0 :
    print(quotient)
else :
    print("undefined")