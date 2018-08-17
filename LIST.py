#Q1
A=[]
n=int(input("enter total no. of value:"))
for x in range(n):
    x=input("enter item:")
    A.append(x)
print (A)

#Q2
B=['google','apple','facebook','microsoft','tesla']
A.extend(B)
print(A)

#Q3
A=['L',1,3,'L',]
print("Total count :",A.count('L'))

#Q4)
A=[]
n=int(input("enter total no. of value:"))
for x in range(n):
    x=int(input("enter item:"))
    A.append(x)
A.sort()
print("A:",A)


#Q5)
A=[]
B=[]
n=int(input("enter total no. of value in list A:"))
for x in range(n):
    x=int(input("enter item:"))
    A.append(x)
n2=int(input("enter total no. of value in list B:"))
for x in range(n2):
    x=int(input("enter item:"))
    B.append(x)
A.sort()
B.sort()
print("Sorted list A:",A)
print("Sorted list B:",B)
A.extend(B)
A.sort()
C=A
print('Merged sorted list :',C)
#Q6
LIST=[]
n=int(input("enter total no. of value:"))
for x in range(n):
    x=int(input("enter numbers:"))
    LIST.append(x)
even=0
odd=0
for j in LIST:
    if j%2==0:
        even+=1
    else:
        odd+=1
print('Total even numbers:',even)
print('Total odd numbers:',odd)
