'''take space separtor inputfor user and print altnernate elements'''
num=list(map(int,input().split(" ")))
for i in range(0,len(num),2):
    print(num[i])
    