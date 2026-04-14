name = "John"
# we can print many words in different lines using tripple quotes in python
print("""Hello """ + name +"""
World lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.""")

print(name[0]) # this will print the first character of the string

#loop in string to print each character in a string
for i in name:
    print(i)

#length of a string
print(len(name)) # this will print the length of the string

# slicing in string

print(name[0:2]) # this will print the first 2 characters of the string
#only 0 and 1 will be printed because the end index is exclusive 

print(name[:3]) # this will print the first 3 characters of the string
print(name[1:4]) # this will print the string from the second character to the end of the string
print(name[-3:len(name)-1]) # this will print the last 3 characters of the string except the last character
print(name[-3:-1]) # this will print the last 3 characters of the string
print(name[::2]) # this will print every second character of the string