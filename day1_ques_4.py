money=int(input())
a=int(input())
b=int(input())
c=int(input())
price_apple= 15*a
price_banana=4*b
price_orange=8*c
sum=price_apple+price_banana+price_orange
if sum>=money:
    print("cheated")
else:
    print("not cheated")