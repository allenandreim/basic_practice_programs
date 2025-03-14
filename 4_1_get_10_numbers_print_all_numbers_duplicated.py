# get 10 number
# check all duplicated
# print all duplicated

# Get 10 numbers
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

# check all duplicated
duplicate_numbers = set(num for num in numbers if numbers.count(num) > 1)

if duplicate_numbers:
    print("Duplicate numbers:", list(duplicate_numbers))  # print all duplicated
else:
    print("No duplicate numbers found.")
