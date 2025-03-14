# get a number
# stop if invalid
# sort numbers descending order

# get a number
numbers = []
while True :
    try :
        num = float(input("type a number (input invalid to stop): "))
        numbers.append(num)
    except ValueError :
        if numbers :
            numbers.sort(reverse=True)  # sort numbers in descending order
            print(numbers)  # print sorted numbers
        else :
            print("no numbers entered")
        print("invalid")  # stop if invalid
        break