 #  7.2 how many even number are in the list
num=list(map(int,input().split(",")))
count=0
for i in range(1,len(num),2):
    count+=1
print(count)
