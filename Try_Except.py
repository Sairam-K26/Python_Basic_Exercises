# try-except block
# try:
#     # code to be executed
# except:
#     # code to handle exceptions

def divi(a,b):
    try:
        a/b
    except :
        print("ZeroDivisionError")
divi(5,0)
#Output: ZeroDivisionError
divi(6/2)
#Output: 3.0

#Exception as error statment
def divi(a,b):
    try:
        a/b
    except ZeroDivisionError as error:
        print(error)
divi(5,0)
#Output: division by zero
divi(6,2)
#Output: None

#accept two strings change it to integers and divide them if error then execute the type of error with try and except
#Example
def divi(a,b):
    try:
        a=int(a)
        b=int(b)
        a/b
    except Exception as error:
        print(error)
divi("5","0")
#Output: division by zero
divi("6","2")
#Output: None
divi("sai","2")
#Output: invalid literal for int() with base 10: 'sai'

#multiple try except block
def divi(a,b):
    try:
        a=int(a)
        b=int(b)
        a/b
    except ZeroDivisionError as error:
        print(error)
    except ValueError as error:
        print(error)
    except Exception as error:
        print(error)
divi("5","0")
#Output: division by zero
divi("6","2")
#Output: None
divi("sai","2")
#Output: invalid literal for int() with base 10: 'sai'

