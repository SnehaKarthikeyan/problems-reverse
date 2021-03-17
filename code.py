Coding:

n=int(input())
arr = list(input().split())
a=int(input())
rev=[]
count=0
for i in range(0,n):
    if int(arr[i])>=a:
        rev.append(arr[i])
rev=rev[::-1]
for i in range (0, len(rev)-1): 
    print (rev[i], end =" ")
print(rev[len(rev)-1])
