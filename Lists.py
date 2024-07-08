#list
#list are mutrable
#list are ordered
#list are indexed
#list are allow duplicate values
#list are allow different data types
#list are represented by []
#list are created by list() or []

#creating a
#empty list
#Example
a = []
print(a)
#Output: []
#Example
a = list()
print(a)
#Output: []

#list with values
#Example
a = [1,2,3,4,5]
print(a)
#Output: [1, 2, 3, 4, 5]
#Example
a = list((1,2,3,4,5))
print(a)
#Output: [1, 2, 3, 4, 5]

#indexing
#Example
a = [1,2,3,4,5]
print(a[0])
#Output: 1

#length
#Example
a = [1,2,3,4,5]
print(len(a))
#Output: 5

#conditional statement
#empty by boolean representation
#Example
a = []
if a:
    print("Yes")
else:
    print("No")
#Output: No

#Example
a = [1,2,3,4,5]
if 1 in a:
    print("Yes")
#Output: Yes

#or
#Example
a = [1,2,3,4,5]
def check_ele(my_list,element):
    return element in my_list
print(check_ele(a,1))
#Output: True

#loop

a = [1,2,3,4,5]
for i in a:
    print(i)
#Output
#1
#2
#3
#4
#5

#count the ele that how many times it appears in list
#Example
from typing import List
def count_ele(nums: List[int],x:int) -> int:
    res=0
    for i in nums:
        if i==x:
            res+=1
    return res
a = [1,2,3,4,5,1,2,3,4,5]
print(count_ele(a,1))
#Output: 2
#or
a = [1,2,3,4,5,1,2,3,4,5]
print(a.count(1))
#Output: 2

#list Function
#sum
#Example
a = [1,2,3,4,5]
print(sum(a))
#Output: 15
#min
#Example
a = [1,2,3,4,5]
print(min(a))
#Output: 1
#max
#Example
a = [1,2,3,4,5]
print(max(a))
#Output: 5

#sum
def sum_ele(nums):
    res=0
    for i in nums:
        res+=i
    return res
a = [1,2,3,4,5]
print(sum_ele(a))
#Output: 15

#min
def min_ele(nums):
    res=nums[0]
    for i in nums:
        if i<res:
            res=i
    return res
a = [1,2,3,4,5]
print(min_ele(a))
#Output: 1

#max
def max_ele(nums):
    res=nums[0]
    for i in nums:
        if i>res:
            res=i
    return res
a = [1,2,3,4,5]
print(max_ele(a))
#Output: 5

#append
#Example
a = [1,2,3,4,5]
a.append(6)
print(a)
#Output: [1, 2, 3, 4, 5, 6]

#implement a function where it append the elements not a single element  of end of the list and return modified list with loop
def append_ele(nums,ele):
    for i in ele:
        nums.append(i)
    return nums
a = [1,2,3,4,5]
b = [6,7,8]
print(append_ele(a,b))
#Output: [1, 2, 3, 4, 5, 6, 7, 8]

#without inbuilt append
def append_ele(nums,ele):
    for i in ele:
        nums+=[i]
    return nums
a = [1,2,3,4,5]
b = [6,7,8]
print(append_ele(a,b))
#Output: [1, 2, 3, 4, 5, 6, 7, 8]

#pop
#Example
a = [1,2,3,4,5]
a.pop()
print(a)
#Output: [1, 2, 3, 4]
#Example
a = [1,2,3,4,5]
a.pop(0)
print(a)
#Output: [2, 3, 4, 5]

#implement a function where it removes the given index element
def remove_index(nums,index):
    nums.pop(index)
    return nums
a = [1,2,3,4,5]
index=2
print(remove_index(a,index))
#Output: [1, 2, 4, 5]
#to pop lastn elemnts in the list and ensure it is been after 0 and within length of list with while
def remove_last_n_elements(nums,n):
    while n>0:
        nums.pop()
        n-=1
    return nums
a = [1,2,3,4,5]
n=2
print(remove_last_n_elements(a,n))
#Output: [1, 2, 3]

#find index 
#Example
a = [1,2,3,4,5]
print(a.index(3))
#Output: 2

#find index of first occurance of the target wihout inbuilt index()
def find_index(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1
a = [1,2,3,4,5]
target=3
print(find_index(a,target))
#Output: 2

#slicing
#Example
a = [1,2,3,4,5]
start,end = 1,4
print(a[start:end])
#Output: [2, 3, 4]
#print last 3 elements of the list
def get_last_n_elements(nums,n):
    return nums[len(nums)-n:]
a = [1,2,3,4,5]
n=3
print(get_last_n_elements(a,n))
#Output: [3, 4, 5]

#with negative indexing
def get_last_n_elements(nums,n):
    return nums[-n:]
a = [1,2,3,4,5]
n=3
print(get_last_n_elements(a,n))
#Output: [3, 4, 5]

#Tuples
#Tuples are immutable
#Tuples are ordered
#Tuples are indexed
#Tuples allow duplicate values
#Tuples allow different data types
#Tuples are represented by ()
#Tuples are created by tuple() or ()
#creating a
#empty tuple
#Example
a = ()
print(a)
#Output: ()
#Example
a = tuple()
print(a)
#Output: ()
#Example
a = (1,2,3,4,5)
print(a)
#Output: (1, 2, 3, 4, 5)
#Example
a = tuple((1,2,3,4,5))
print(a)

#indexing
#Example
a = (1,2,3,4,5)
print(a[0])
#Output: 1

#implement a creat_pair(name: str,age:int) ->Tuple[str,int] function which should combine name and age into tuple and retrn it name as first ele and age as second
def creat_pair(name,age):
    return (name,age)
name="John"
age=36
print(creat_pair(name,age))
#Output: ('John', 36)

 

