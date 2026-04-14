a = "1"
b = "2"
c = a + b
print(c)

# In the above code, we are concatenating the strings "1" and "2" to get "12". The + operator is used for concatenation in this case.
# what is concatenation?
# concatenation is the operation of joining two strings together. In this case, the strings "

# Type casting in python

d = int(a) + int(b)
print(d)

# In the above code, we are converting the strings "1" and "2" to integers using the int() function, and then adding them together to get 3. The int() function is used for type casting in this case.


# name = "Deepak"
# e = int(name)
# print(e)
# this will give an error because we cannot convert a string that does not represent a number to an integer 

#types of type casting in python
# implicit type casting
x = 5
y = 2.5 
z = x + y
print(z)
# In the above code, we are adding an integer (5) and a float (2.5) together. Python automatically converts the integer to a float before performing the addition, resulting in 7.5. This is an example of implicit type casting.

# explicit type casting
k = "5"
l = "2.5"
m = int(k) + float(l)
print(m)
# In the above code, we are explicitly converting the string "5" to an integer using