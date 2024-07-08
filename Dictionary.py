#Dictinary
#Dictionary is a collection of key-value pairs.
#Dictionary is mutable.
#Dictionary is unordered.
#Dictionary is represented by {}.
#Dictionary is created by dict() or {}.
#creating a
#empty dictionary
#Example
a = {}
print(a)
#Output: {}
#Example
a = dict()
print(a)
#Output: {}

#dictionary with values
#Example
a = {"name":"John","age":25}
print(a)
#Output: {'name': 'John', 'age': 25}
#Example
a = dict(name="John",age=25)
print(a)
#Output: {'name': 'John', 'age': 25}
#Example
my_dict={}
my_dict["name"]="John"
my_dict["age"]=25
print(my_dict)
#Output: {'name': 'John', 'age': 25}

#create a dit and map name to age and return
#Example
def create_dict(name,age):
    return {"name":name,"age":age}
print(create_dict("John",25))
#Output: {'name': 'John', 'age': 25}

#given a list of words so we take a list of string and map each to its index 
#Example
def map_index(a):
    b = {}
    for i in range(len(a)):
        c=a[i]
        b[c]=i
    return b
print(map_index(["hello","world","hello"]))
#Output: {'hello': 2, 'world': 1}

# dict operation
#no duplicate key
#Example
a = {"name":"John","age":25}
a["name"]="Smith"
print(a)
#Output: {'name': 'Smith', 'age': 25}

#values duplicate
#Example
a = {"name":25,"name2":25}
print(a)
#Output: {'name': 25, 'name2': 25}

#nested dict
#Example
a = {"name":"John","age":25,"address":{"city":"New York","state":"NY"}}
print(a)
#Output: {'name': 'John', 'age': 25, 'address': {'city': 'New York', 'state': 'NY'}}

#in
#Example
a = {"name":"John","age":25}
print("name" in a)
#Output: True

#dict loop
#Example
a = {"name":"John","age":25}
for key in a:
    print(key,a[key])
#Output: name John
#Output: age 25

#using .items()
#Example
a = {"name":"John","age":25}
for key,value in a.items():
    print(key,value)
#Output: name John
#Output: age 25

#get a dict of names and ages and return list of names
#Example
def get_names(a):
    res=[]
    for name in a:
        res.append(name)
    return res
print(get_names({"name":"John","age":25}))
#Output: ['name', 'age']

#get the values of key 
#Example
def get_values(a):
    res=[]
    for key in a:
        b=a[key]
        res.append(b)
    return res
print(get_values({"name":"John","age":25}))
#Output: ['John', 25]

#take a string and return the dictionary with count of each character in word as caharacter as key and count as value and check if key is exist first
#Example
def count_char(a):
    b={}
    for i in a:
        if i in b:
            b[i]+=1
        else:
            b[i]=1
    return b
print(count_char("hello"))
#Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

#dict remove
#Example
a = {"name":"John","age":25}
a.pop("name")
print(a)
#Output: {'age': 25}

#Example
a = {"name":"John","age":25}
del a["name"]
print(a)
#Output: {'age': 25}

#Example
a = {"name":"John","age":25}
a.pop("sai",0)
print(a)
#Output: {'name': 'John', 'age': 25}

#Example
a = {"name":"John","age":25}
a.popitem()
print(a)
#Output: {'name': 'John'}

#Example
a = {"name":"John","age":25}
a.clear()
print(a)
#Output: {}

#Example
a = {"name":"John","age":25}
del a
#print(a)
#Output: NameError: name 'a' is not defined

#accept a dictionary and remove the all key specified with for loop 
#Example
def remove_key(a,b):
    for i in b:
        a.pop(i,0)
    return a
print(remove_key({"name":"John","age":25},["name","age"]))
#Output: {}

#accept a dict and return values
#Example
def get_values(a):
    res=[]
    for key in a:
        res.append(a[key])
    return res
print(get_values({"name":"John","age":25}))
#Output: ['John', 25]

def getvalues(a):
    return list(a.values())
print(getvalues({"name":"John","age":25}))
#Output: ['John', 25]





