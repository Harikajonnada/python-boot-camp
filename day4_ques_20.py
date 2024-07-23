'''mr x is trting to create a new paasword for his insts acc this sare req conditions for creating a new password 
con1 min len is 8 max ken is 15 
con2 only @/ is allowed in pw con
con3 no spaces are allowed
 con4 only alpha numeric are allowed 
  ur suposs to prnt weak if len exact 8 medium len bwt 8-12 storng len is bwt 12-15 '''

n="harikagoud@123"
l=len(n) 
count=0 
for i in n: 
    if(i=='@' or i=='/' and i!=' '):
         count+=1
         break
if(count==0 ):
      print("please follow rules")
elif(l<8):
       print("please follow rules")
elif(l>=8 and l<12):
       print("password is weak")
elif(l>8 and l<12):
     print("password is medium")
elif(l>12 and l<=15):
     print("password is strong")
