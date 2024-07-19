my_list=list(map(int,input().split(",")))
#my_list.append(2)
#print(my_list)
print("1.append")
print("2.pop")
print("3.sort")
print("4.length")
print("5.exit")
print("enter your choice")
choice=int(input())
if choice==1:
    my_list.append(9)
    print(*my_list)
elif choice==2:
    my_list.pop(2)
    print(*my_list)
elif choice==3:
    my_list.sort()
    print(*my_list)
elif choice==4:
    print(len(my_list))
else:
    exit()
    print("exit")

