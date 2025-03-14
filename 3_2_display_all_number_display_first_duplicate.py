# get 10 numbers
# display all numbers, showing only the first entry for duplicates
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

# display all numbers, showing only the first entry for duplicates
seen = set()
result = []
for num in numbers:
    if num not in seen:
        result.append(num)
        seen.add(num)

# print result
print("numbers (first entry only for duplicates):", result)