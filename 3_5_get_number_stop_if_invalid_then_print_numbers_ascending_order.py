# get a number
# stop if invalid
# print numbers in ascending order

# get a number
numbers = []
while True :
    try :
        num = float(input("type a number (input invalid to stop): "))
        numbers.append(num)
    except ValueError :
        if numbers :
            numbers.sort()  # sort numbers in ascending order
            print(numbers)  # print sorted numbers
        else :
            print("no numbers entered")
        print("invalid")  # stop if invalid
        break
