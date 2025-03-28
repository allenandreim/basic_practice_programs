# type something with space
# remove characters in the beginning of the string without using removeprefix() function
# print output

# type something with space
phrase = input("enter the original string: ")
prefix_to_remove = input("enter the prefix to remove: ")

# remove characters in the beginning of the string without using removeprefix() function
if phrase[:len(prefix_to_remove)] == prefix_to_remove:
    result = phrase[len(prefix_to_remove):]
else:
    result = phrase   

# print output
print(result)