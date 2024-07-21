'''*****reverse of number '''
n=int(input())
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
print(rev)
print(type(rev)) # to know datatype
#print(int(rev)) #---int used to convert str to int
ans=int(rev)
print(type(ans))