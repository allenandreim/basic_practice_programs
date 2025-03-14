# get a number
# stop if invalid
# print smallest

# get a number
numbers = []

while True :
    try:
        num = float(input("type a number(input invalid to stop): "))
        numbers.append(num)
    except ValueError :
        if numbers :     
            print("lowest number:", min(numbers))
        else :
            print("no numbers entered")
        print("invalid")            
        break
    
