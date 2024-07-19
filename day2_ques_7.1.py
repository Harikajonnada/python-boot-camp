#7.3 given with space sep integer list find num even ele & odd
num=list(map(int,input().split(" ")))
even=0
odd=0
for i in range(len(num)):
    if(num[i]%2==0):
        even+=1
    else:
        odd+=1
print(even)       
print(odd)
