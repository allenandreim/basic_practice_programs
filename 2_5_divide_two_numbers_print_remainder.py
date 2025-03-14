# get 2 numbers
# divide 2 numbers
# print remainder

# get 2 numbers
num1 = float(input("1st number(dividend): "))
num2 = float(input("2nd number(divisor): "))

# divide num1 to num2 (use % to get remainder)
remainder = num1 % num2

# restrict 0 in divisor 
if num2 != 0 :
    print("the remainder is:", remainder)
else :
    print("undefined")