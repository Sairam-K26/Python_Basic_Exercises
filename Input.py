#input
#to get a user input and return in user console
#Example
def read_input():
    a=input()
    return a
print(read_input())
#Output: user input
#prints on same line

#type conversion
#default it will be string
#Example
def type_conversion(a):
    return str(a)
print(type_conversion(25))
#Output: 25

#Example
def type_conversion(a):
    return int(a)
print(type_conversion("25"))
#Output: 25
#Example
def type_conversion(a):
    return float(a)
print(type_conversion("25"))
#Output: 25.0

#parse input
#Example
def parse_input(a):
    return a.split()
print(parse_input("John 25"))
#Output: ['John', '25']

#Example
def parse_input(a):
    return a.split(",")
print(parse_input("John,25"))
#Output: ['John', '25']

#Example
def parse_input(a):
    return a.split(",",1)
print(parse_input("John,25,sai"))
#Output: ['John', '25,sai']

#implement the read_integer() function , it should read a line without printing and return a list of integers.the numbers will be seperated by commas
#Example
def read_integer():
    return list(map(int,input().split(",")))

print(read_integer())
#Output: 1,2,3,4,5
#Output: [1, 2, 3, 4, 5]

def read_integers():
    line-=input()
    list_of_strings = line.split(",")
    list_of_int=[]
    for string in list_of_strings:
        list_of_int.append(int(string))
    return list_of_int
print(read_integers())
#Output: 1,2,3,4,5
#Output: [1, 2, 3, 4, 5]

#take 2 input from user  and return its sum
#Example
def input_sum():
     a=list(map(int,input().split(",")))
     return a[0]+a[1]
print(input_sum())
#Output: 1,2
#Output: 3

def add_two_numbers():
    line=input()
    numbers=line.split(",")
    return int(numbers[0])+int(numbers[1])  
print(add_two_numbers())
#Output: 1,2
#Output: 3




