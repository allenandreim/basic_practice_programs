# get a numbers
# stop if invalid
# get the average of number

# get a number
numbers = []

while True:
    try:
        num = float(input("Enter a number (invalid to stop): "))
        numbers.append(num)
    except ValueError:  # stop if invalid
        if numbers:
            average = sum(numbers) / len(numbers)  # get the average of numbers
            print("average:", average)
        else:
            print("no numbers entered.")
        print("invalid")
        break