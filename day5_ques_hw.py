'''upper triangle
lower triangle
parallelogram
    ***
     ***
        ***
rhombus
num pyramid'''


'''n=int(input())
for i in range(n):
    for j in range(n):
        if(i>j):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()'''

n=int(input())
for i in range(n):
    for j in range(n):
        if(i<j):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()


'''n=int(input())
for i in range(0,n):
    for j in range(1,i+1):
            print("*",end=" ")
    print()'''
