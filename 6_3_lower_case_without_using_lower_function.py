# type something   
# make characters lower without using lower() function
# print output

# type something 
phrase = input("enter a string: ")
result = ""

# make characters lower without using lower() function
for char in phrase:
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32) 
    else:
        result += char  

# print output
print(result)