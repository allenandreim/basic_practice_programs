# get 10 numbers
# find unique numbers
# print result

# get 10 numbers
num1 = float(input("1st number: "))
num2 = float(input("2nd number: "))
num3 = float(input("3rd number: "))
num4 = float(input("4th number: "))
num5 = float(input("5th number: "))
num6 = float(input("6th number: "))
num7 = float(input("7th number: "))
num8 = float(input("8th number: "))
num9 = float(input("9th number: "))
num10 = float(input("10th number: "))

numbers = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]

# find unique numbers
unique_numbers = [num for num in numbers if numbers.count(num) == 1]

# print results
if unique_numbers:
    print("Unique numbers:", unique_numbers)
else:
    print("No unique numbers found.")

