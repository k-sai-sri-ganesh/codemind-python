a,b=map(int,input().split())
c=max(a,b)
d=min(a,b)
x=c-d
if x==1 or x==9:
    print("Yes")
else:
    print("No")