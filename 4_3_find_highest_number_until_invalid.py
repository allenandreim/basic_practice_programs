# get a numbers
# stop if invalid
# print highest number

# get a numbers
numbers = []

while True:
    try:
        num = float(input("Enter a number (invalid to stop): "))
        numbers.append(num)
    except ValueError:   # stop if invalid
        if numbers:
            print("highest number:", max(numbers))  # print highest number
        else:
            print("no numbers entered.")
        print("invalid")
        break
