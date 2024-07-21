#find the elements present in k+N index
n=list(map(int,input().split()))
N=int(input())
k=int(input())
l=len(n)
if(len(n)<k+N):
    print("error")
else:
    #print(n[k+N])
    for i in range(len(n)):
        print(n[k+N])
        break
# for i in range(len(n))
#if(i==k+N)
#print(n[i])




'''print the element in particular index'''
