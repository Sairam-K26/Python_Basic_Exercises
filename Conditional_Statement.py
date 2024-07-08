#comparision operator
a=10
b=20
c=a==b
print(c)  # Output: False
c=a!=b
print(c)  # Output: True
c=a>b
print(c)  # Output: False
c=a<b
print(c)  # Output: True
c=a>=b
print(c)  # Output: False
c=a<=b
print(c)  # Output: True

#if condtion
a=10
b=20
if a>b:
    print("a is greater than b")
print("lesser")  # Output: lesser

#if scope
a=10
b=20
if a>b:
    print("a is greater than b")
print("lesser")  # Output: lesser

#if else
a=10
b=20
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")
print("lesser")  # Output: b is greater than a

#if elif else
a=10
b=20
if a>b:
    print("a is greater than b")
elif a<b:
    print("b is greater than a")
else:
    print("a is equal to b")
print("lesser")  # Output: b is greater than a

#logic condition
a=10
b=20
c=30
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
else:
    print("c is greater")
print("lesser")  # Output: c is greater

#or
a=10
b=20
c=30
if a>b or a>c:
    print("a is greater")
elif b>a or b>c:
    print("b is greater")
else:
    print("c is greater")
print("lesser")  # Output: c is greater

#truthy falsy
a=10
if a:
    print("a is true")
else:
    print("a is false")
print("lesser")  # Output: a is true




