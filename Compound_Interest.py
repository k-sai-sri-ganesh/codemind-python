p=int(input())
r=int(input())
t=int(input())
compound=p * (pow((1 + r / 100), t))-p
print("%.2f"%compound)