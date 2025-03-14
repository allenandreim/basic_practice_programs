# get numbers
# print duplicate if number is duplicated, print unique if number is unique
# stop program if input is invalid

numbers = [] # initialize number

# get numbers
while True:
    try :
        num = float(input("type a number(input invalid to stop): "))
        if num in numbers :
            print("duplicate")

        else :
            print("unique")
        numbers.append(num)
    except ValueError :
        print("invalid")
        break