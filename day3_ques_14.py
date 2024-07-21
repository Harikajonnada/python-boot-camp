'''missing in array'''
a=list(map(int,input().split()))
#n=int(input())
n=len(a)+1
k=sum(a)
sum=n*(n+1)//2 
print(sum-k)