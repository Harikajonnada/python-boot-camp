'''find even or odd
find greatest of 3
sum of elements in array
**find peak element
max element array
second max element in array
reverse without using builtin function
sum of square of given num
find sum suqres of even and odd digits
check whether palindrome
to print 1st n fabbnoic 
'''  

'''n=int(input())
if(n%2==0):
    print("the numder is even")
else:
    print("the number is odd")'''

'''a=int(input())
b=int(input())
c=int(input())
if(a>b and a>c):
    print("the greatest number is",{a})
elif(b>a and b>c):
    print("the greatest number is",{b})
else:
    print("the greatest number is",{c})'''

'''n=list(map(int,input().split()))
sum=0
for i in n:
    sum+=i
    print(sum)'''


'''n=list(map(int,input().split()))
max=n[0]
for i in range(len(n)):
    if(n[i]>max):
        max=n[i]
print(max)   '''

'''n=list(map(int,input().split()))
max=n[0]
for i in range(len(n)):
    if(n[i]>max):
        max=n[i]
print(max-1)   '''


'''n=int(input())
a=0
num=0
while n>0:
    a=n%10
    num=num*10+a
    n=n//10
print(num)'''

'''n=int(input())
sum=0
while n>0:
    a=n%10
    sum=sum+a**2
    n=n//10
print(sum)'''


'''n=int(input())
sum=0
while n>0:
    a=n%10
    if(a%2==0):
        sum=sum+a**2
    n=n//10
print(sum)'''


'''n=int(input())
sum=0
while n>0:
    a=n%10
    if(a%2!=0):
        sum=sum+a**2
    n=n//10
print(sum)'''

n=int(input())
s=n
r=0
while(n>0):
    num=n%10
    r=r*10+num
    n=n//10
if r==s:
     print("palindrome")
else:
    print("not palindrome")
