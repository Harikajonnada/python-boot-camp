#   ascii values
'''A=65,0=48,a=97'''
'''to print asci value'''
#print(ord('A'))
'''to print asci to alpha'''
#print(chr(70))
'''check how many vowels and  are in string'''
s="Harikagoud"
con="bcdfghjklmnprstvwxyz"
count=0
c=0
n=s.lower()
v="aeiouAEIOU"
for i in s:  
    if(i in v):#----to vowels
        count+=1
print(count)
for i in n:
    if(i in con ):
        c+=1
print(c)