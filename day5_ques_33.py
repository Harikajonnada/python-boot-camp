#sum of number in string
s="hello 123" 
c="0123456789"
sum=0
for i in s:
    if(i in c):
        sum+=int(i)
print(sum)


'''=input()
sum=0
for i in s:
    if(ord(i)>=48 and ord(i)<=57):
        sum+=int(i)
print(sum)'''

"reverse of number in string "
'''s="hello 123" 
c="0123456789"
r=""
for i in s:
    if(i in c):
        r+=i
print(int(r))
while int(r)>0: 
    a=r%10
    r=r+str(a)
    r=r//10
print(int(r))'''



''' to print all captial letter in increment string'''
'''s=input()
sum=0
for i in s:
    if(ord(i)>=65 and ord(i)<=91):
        sum+=i
print(sum)'''