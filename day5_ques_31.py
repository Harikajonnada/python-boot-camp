'''write a program to print all the vowels followed by consonents'''
s="harikagoud"
con="bcdfghjklmnprstvwxyz"
c=""
n=s.lower()
v="aeiouAEIOU"
for i in s:  
    if(i in v):#----to vowels
     c+=i
for i in n:
    if(i in con ):
       c+=i
print(c)