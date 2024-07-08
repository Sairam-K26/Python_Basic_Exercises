#length

#The length of a string is the number of characters in the string.
#The len() function returns the length of a string.
#Example
#Get the length of the string:
a = "Hello, World!"
print(len(a))
#Output: 13

#get longer word out of word 1 and word2 if both are same return word 1
def get_longer_word(word1,word2):
    if len(word1)>=len(word2):
        return word1
    return word2
word1="Hello"
word2="World"
print(get_longer_word(word1,word2))  # Output: Hello

#string indexing
#Access characters in a string by referring to its index inside square brackets [].
#Example
#Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])
#Output: e

#looping string
#Loop through the letters in the word "banana":

str="hello world"
length=len(str)
for i in range(length):
    print(str[i])
#Output
#h
#e
#l
#l
#o
#
#w
#o
#r
#l
#d


for x in "banana":
    print(x)
#Output
#b
#a
#n
#a
#n
#a

def concatenate(s1,s2):
    s3=s1+s2
    if len(s3)<10:
        return s3
    return "string is too long"
s1="Hello"
s2="World"
print(concatenate(s1,s2))  # Output: HelloWorld

s1="Hellllllllllllo"
s2="worl    d"
print(concatenate(s1,s2))  # Output: string is too long

#slicing
#You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.
#Example
#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
start,end = 1,5
print(b[start:end])

#now give as the same and the start will be always valid index but if suppose the end index is not valid give the output as empty string
def get_substring(input_string,start,end):
    if end>len(input_string):
        return ""
    return input_string[start:end]
input_string="Hello, World!"
start,end=1,5
print(get_substring(input_string,start,end))  # Output: ello
input_string="hello"
start,end=1,10
print(get_substring(input_string,start,end))  # Output:

#no start
#Example
#Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])
#Output: Hello
#no end
#Example
#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])
#Output: llo, World!
#no start, no end
#Example
#Get the whole word:
b = "Hello, World!"
print(b[:])
#Output: Hello, World!

#print first  n caharacters
def get_first_n_characters(input_string,n):
    return input_string[:n]
input_string="Hello, World!"
n=5
print(get_first_n_characters(input_string,n))  # Output: Hello

#last n characters 
def get_last_n_characters(input_string,n):
    return input_string[-n:]
input_string="Hello, World!"
n=5
print(get_last_n_characters(input_string,n))  # Output: World!

#reversing a string with slicing
def reverse_string(input_string):
    return input_string[::-1]
input_string="Hello, World!"
print(reverse_string(input_string))  # Output: !dlroW ,olleH

#reversing
#To reverse a string, use the reversed() function.
#Example
#Reverse the string:
a = "Hello, World!"
print(''.join(reversed(a)))
#Output: !dlroW ,olleH

#immutable
#Python strings are immutable, which means they cannot be changed after they are created.

#remove 4th character and give the string
def remove_4th_character(input_string):
    return input_string[:3]+input_string[4:]
input_string="Hello, World!"
print(remove_4th_character(input_string))  # Output: Helo, World!

#string format
#As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
#Example
#age = 36
#txt = "My name is John, I am " + age
#TypeError: can only concatenate str (not "int") to str
#But we can combine strings and numbers by using the format() method!
#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
#Example
#Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#Output: My name is John, and I am

# or f method
#Example
txt = f"My name is John, and I am {age}"
    