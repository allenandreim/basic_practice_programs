# get a nummber
# stop if invalid
# print most frequent duplicate

# get a nummber
numbers = []

while True:
    try:
        num = float(input("Enter a number (invalid to stop): "))
        numbers.append(num)
    except ValueError:
        if not numbers:
            print("No numbers entered.")
            break
        # count duplicates
        duplicates = {n: numbers.count(n) for n in numbers if numbers.count(n) > 1}
        if duplicates:
            most_frequent = max(duplicates, key=duplicates.get)  # print most frequent duplicate
            print("Most frequent duplicate:", most_frequent)
        else:
            print("No duplicates found.")
        print("Invalid input. Exiting...")
        break
