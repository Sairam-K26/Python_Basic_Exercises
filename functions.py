#function
def add(a,b):
    return a+b
print(add(10,20))  # Output: 30
#indentation matters
#function is called by its name and ()  like add()
#must be declared before they are going to be used

#function parameter
def greet(name):
    print("Hello, " + name)
greet("John")  # Output: Hello, John

#multiple parameter
def add(a,b,c):
    return a+b+c
print(add(10,20,30))  # Output: 60

#return
def add(a,b):
    return a+b
result=add(10,20)
print(result)  # Output: 30

#type hint
def add(a:int,b:int)->int:
    return a+b
result=add(10,20)
print(result)  # Output: 30

#scope
#global variable
a=10
def test():
    print(a)
test()  # Output: 10

#local variable
def test():
    a=10
    print(a)
test()  # Output: 10

a=10
def test():
    print(11)
test()  # Output: 11 
print(a)  # Output: 10

#global vs local
def test():
    a=11
    print(a)
test()  # Output: 11
print(a)  # error because it cant be assesed outside function

#default argument
def greet(name,msg="Good Morning"):
    print("Hello",name+", "+msg)
greet("John")  # Output: Hello John, Good Morning


