# input full name
# make it in pascal case 
# print output 

# input full name
name = input("full name: ")

# make it in pascal case 
words = name.split()
pascase_name = "".join(word.capitalize() for word in words)

# print output 
print(pascase_name)