'''lcm of 2 numbers'''
a=int(input())
b=int(input())
c,d=a,b
while b!=0:
    a,b=b,a%b
    gcd=a
    lcm=(c*d)//gcd
print(lcm)