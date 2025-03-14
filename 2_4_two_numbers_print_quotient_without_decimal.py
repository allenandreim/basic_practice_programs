# get 2 numbers
# divide num1 to num2
# restrict 0 in divisor 
# print result (no decimal)

# get 2 numbers
num1 = float(input("1st number(dividend): "))
num2 = float(input("2nd number(divisor): "))


# restrict 0 in divisor 
if num2 != 0 :
    quotient = int(num1 // num2)  # divide num1 to num2
    print("quotient (without decimal):", quotient)
else :
    print("undefined") 