'''INPUT HELLLO-----WORID--------> OUTPUT=-----------HELLO WORLD'''
s=input()
count=""#count=0
new=""
for i in s:
    if(i=='-'):
        count+=i #count+=1
    else:
        new+=i
print(count+new) #print("-"*count+new)