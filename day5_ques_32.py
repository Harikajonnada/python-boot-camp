'''print the unquie char in string'''
s="harikagoud"
ans=""
for i in s:
    if(i not in ans):
        ans+=i
print(ans)
    