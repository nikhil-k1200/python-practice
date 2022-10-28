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

name=input("Enter Name: ")
i=1
for x in name:
    if i!=1:   # do not print if i=2
        print('The letter at index',i,'is',x)
    i+=1