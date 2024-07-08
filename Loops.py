#while loops
#while loops are used to execute a block of code multiple times
#as long as a condition is true.
#syntax
#while condition:
#    code block
#example
a=1
while a<6:
    print(a)
    a+=1
#output
#1
#2
#3
#4
#5

#while loop multiples
n=10
while n<100:
    print(n)
    n+=10
#output
#10
#20
#30
#40
#50
#60
#70
#80
#90

#for loop
#loops through a sequence of items
#syntax
#for item in sequence:
#    code block
#example
fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)
#output
#apple
#banana
#cherry

#start and end
for x in range(2,6):
    print(x)
#output
#2
#3
#4
#5

#step
for x in range(2,30,3):
    print(x)
#output
#2
#5
#8
#11
#14
#17
#20
#23
#26
#29

#for lopps reverse
for x in range(10,0,-1):
    print(x)
#output
#10
#9
#8
#7
#6
#5
#4
#3
#2
#1

#nested loop
adj=["red","big","tasty"]
fruits=["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)
#output
#red apple
#red banana
#red cherry
#big apple
#big banana
#big cherry
#tasty apple
#tasty banana
#tasty cherry

#break , continue , pass
#break
#stops the loop before it has looped through all the items
fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x=="banana":
        break
#output
#apple
#banana
#continue
#stops the current iteration and continues with the next
fruits=["apple","banana","cherry"]
for x in fruits:
    if x=="banana":
        continue
    print(x)
#output
#apple
#cherry
#pass
#pass is a null statement
#it does nothing when executed
fruits=["apple","banana","cherry"]
for x in fruits:
    pass
#output
#nothing





