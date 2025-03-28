# type something with space
# remove spaces without using lstrip() function
# print output

# type something with space
phrase = input("type something with extra spaces in the beginning: ")

# remove spaces without using lstrip() function
index = 0
while index < len(phrase) and phrase[index] == " ":
    index += 1

result = phrase[index:]

print(result)