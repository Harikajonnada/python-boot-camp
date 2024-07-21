'''find duplicate in array'''
a=list(map(int,input().split()))
new=[]
#new.append(a[0]) 
#for i in a:
#    if (i not in new):
 #       new.append(i)
#print(*new)
for i in a:
    if(i in new):
        new.append(i)
print(*new)        
