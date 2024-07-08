# Update the code on the right so that it prints this string is stored in a variable to the console twice. You should be able to accomplish this by only adding one line of code.

message="this string is stored in a variable"
print(message)
print(message)

# There are some strict rules for naming variables, if you
# break any of these rules it will cause an error:
# Variable names can only contain letters, numbers,
# and underscores.
# Variable names can't start with a number.
# Variable names can't contain spaces.
# • Variable names can't be the same as Python
# This will cause an error
# 1st_variable = 10
# This will cause an error
# my variable = 5
# This will cause an error
# calculate total amount = 0
# This will cause an error
# total-amount = 0

# naming conventions:
# Camel case
myVariable = 10
calculateTotalAmount = 0

# Snake case
my_variable = 5
calculate_total_amount = 0

# Pascal case
MyVariable = 7
CalculateTotalAmount = 0

# Variables can be reassigned to different data types.
name="sai"
name=10
print(name)

#multiple assignments
a,b=1,2
print(a)
print(b)
#we can also swap
a,b=b,a
print(a)
print(b)

msg1,msg2 ="world","hello"
msg3,msg4,msg5 ="name","my","is"
print(msg1,msg2,msg3,msg4,msg5)
#we need as Hello world my name is
#swap 
msg1,msg2=msg2,msg1
msg3,msg4,msg5=msg5,msg4,msg3
print(msg1,msg2,msg3,msg4,msg5)

#variable types  in python 
#int
age = 25
print(age)

#float
pi = 3.14
print(pi)

#string
name = "John"
print(name)

#boolean
is_true = True
print(is_true)

#complex
complex_num = 2 + 3j
print(complex_num)

#list
numbers = [1, 2, 3, 4, 5]
print(numbers)

#type of value
print(type(age))
print(type(pi))
print(type(name))
print(type(is_true))
print(type(complex_num))
print(type(numbers))

#type initialisation
age = int(age)
print(age)

#type casting
age = 25
print(age)
print(type(age))
age = float(age)
print(age)
print(type(age))

#type error
# name = "sairam"
# print(type(name))
# name = int(name)
# print(name)
# ValueError

age = "25"
print(age)
print(type(age))
age = int(age)
print(age)
print(type(age))

#empty or None variable
empty = None
print(empty)
print(type(empty))

#variable scope
# Global scope
# A variable that is declared outside of a function is a global variable. It can be accessed from any function in the program.
# Local scope
# A variable that is declared inside a function is a local variable. It can only be accessed from that function.























