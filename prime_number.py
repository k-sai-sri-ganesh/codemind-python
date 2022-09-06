n=int(input())
i=2
if n>1:
    while i<n:
        if n%i==0:
            print("not a prime")
            break
        i+=1
    else:
        print("prime")
else:
    print("not a prime")