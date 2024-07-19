n=int(input())
if n%2==0 and n>0:
    print("postive even")
elif n%2==0 and n<0:
    print("negative even")
elif n<0:
    print("negative odd")
else:
    print("postive odd")
