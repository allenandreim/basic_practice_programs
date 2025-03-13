# get 10 numbers
# check if a number is odd using %2
# print how many odds

# Initialize odd count
odd_count = 0

# Get 10 numbers
num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))
num3 = int(input("3rd number: "))
num4 = int(input("4th number: "))
num5 = int(input("5th number: "))
num6 = int(input("6th number: "))
num7 = int(input("7th number: "))
num8 = int(input("8th number: "))
num9 = int(input("9th number: "))
num10 = int(input("10th number: "))   

#check if a number is odd and count
if num1 % 2 != 0:
    odd_count += 1
if num2 % 2 != 0:
    odd_count += 1
if num3 % 2 != 0:
   odd_count += 1
if num4 % 2 != 0:
    odd_count += 1
if num5 % 2 != 0:
    odd_count += 1
if num6 % 2 != 0:
    odd_count += 1
if num7 % 2 != 0:
    odd_count += 1
if num8 % 2 != 0:
    odd_count += 1
if num9 % 2 != 0:
    odd_count += 1
if num10 % 2 != 0:
    odd_count += 1

# print result
print("There are", odd_count, "odd numbers.")
    
