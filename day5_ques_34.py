'''"asci btw range"
for i in range(32,128):
    print(chr(i),end=" ")'''

'''coverting the integer value into asci value and sum'''
'''s="hello 123" 
c="0123456789"
sum=0
for i in s:
    if(i in c):
        sum+=ord(i)
print(sum) o/p=15o'''

'''s=input()
sum=0
for i in s:
    if(ord(i)>=48 and ord(i)<=57):
        sum+=int(i)
print(sum)'''

''' to print all captial letter in increment string'''
s=input()
sum=0
for i in s:
    if(ord(i)>=65 and ord(i)<=91):
        sum+=i
print(sum)


for i in range(65,91):
    print(chr(i),end=" ")