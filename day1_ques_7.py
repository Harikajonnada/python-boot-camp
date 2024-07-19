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

