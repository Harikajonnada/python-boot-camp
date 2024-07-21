'''find the max element in the given list'''
a=list(map(int,input().split()))
max=a[0]
for i in range(len(a)):
    if(max<a[i]):
        max=a[i]
print(max)

    
