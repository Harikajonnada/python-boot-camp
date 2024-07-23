'''print patter 
*****
*****
*****
*****
*****'''
n=int(input())
for i in range(n):
    for j in range(n):
          print("*",end=" ")
    print()


''' print patterns
 *****
 *****
 *****
 *****
 *****
 '''   
n=int(input())
for i in range(n):
    for j in range(n):
        if(i==j):
            print(" ",end=" ")
        else:
          print("*",end=" ")
    print()