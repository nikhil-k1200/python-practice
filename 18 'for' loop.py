#a="Nikhil Kamble"
#count=0
#for x in a:
#    print(x)
#    count+=1
#print('Total letters are:',count)

#name=input("Enter Name: ")
#i=1
#for x in name:
#    print('The letter at index',i,'is',x)
#    i+=1

#name=input("Enter Name: ")
#i=1
#for x in name:
#    if i!=1:   # do not print if i=2
#        print('The letter at index',i,'is',x)
#    i+=1


# Print 'HEllo world' 10 times
#c=0
#for x in  range(10):    # range(10) means 0 to 9
#    print(c,'Hello World')
#    c+=1


# Print 'HEllo world' 0-20 for even numbers only
#c=0
#for x in  range(21):    # range(21) means 0 to 20
#    if x%2==0:
#       print(c,'Hello World')
#    c+=1


# Print 'Hello world' 20 times for odd numbers only
#c=0
#for x in  range(20):
#    if x%2!=0:
#       print(c,'Hello World')
#    c+=1

#c=1
#for x in  range(1,20,2):    # from 1 to 20 with increment of 2
#   print(c,'Hello World')
#   c+=2


# print in descending order
#c=10
#for x in  range(10,1,-1):    # from 10 to 2 with decrement of 1
#   print(c,'Hello World')
#   c-=1

#c=10
#or x in  range(10,0,-1):    # from 10 to 1 with decrement of 1
#   print(c,'Hello World')
#   c-=1



# find sum of entered numbers from the list
sum=0
list=eval(input("Enter list values:"))
for x in list:
    sum=sum+x
print("Sum = ",sum)