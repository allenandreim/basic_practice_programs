# input full name
# make it in snake case
# print output 

# input full name
name = input("full name: ")

# make it in snake case
words = name.split()
sncase_name = "_".join(word.lower() for word in words)

# print output 
print(sncase_name)
