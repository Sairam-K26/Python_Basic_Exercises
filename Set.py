#set
#unordered
#no duplicate
#no indexing
#no different data types
#represented by {}
#created by set() or {}
#
#creating a
#empty set
#Example
a = {}
print(a)
#Output: {}
#Example
a = set()
print(a)
#Output: set()

#given a list of numbers create set with those with for loop
#Example
a = [1,2,3,4,5]
b = set()
for i in a:
    b.add(i)
print(b)
#Output: {1, 2, 3, 4, 5}

#remove
#Example
a = {1,2,3,4,5} 
a.remove(1)
print(a)
#Output: {2, 3, 4, 5}

#in
#Example
a = {1,2,3,4,5}
if 1 in a:
    print("Yes")
#Output: Yes

# implement function count_uniqur_words which accept a list of strings and return the no of uniquewords.if the list is empty return 0
#Example
def count_unique_words(a):
    b = set()
    for i in a:
        b.add(i)
    return len(b)
print(count_unique_words(["hello","world","hello"]))
#Output: 2

def unique(a):
    b = set(a)
    count = 0
    for i in b:
        count += 1
    return count
print(unique(["hello","world","hello"]))
#Output: 2

def unique2(a):
    b=set(a)
    return len(b)
print(unique2(["hello","world","hello"]))
#Output: 2

#find duplicate with loop
#Example
a = [1,2,3,4,5,1,2,3]
b = set()
for i in a:
    if a.count(i) > 1:
        b.add(i)
print(b)
#Output: {1, 2, 3}

def dupli(a):
    b=set(a)
    return len(b)<len(a)
print(dupli([1,2,3,4,5,1,2,3]))
#Output: True




