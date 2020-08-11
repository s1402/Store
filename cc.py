for __ in range(int(input())):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    c=l[0]
    if x>=c:
        print(n)
        continue
    else:
        d=0  
        while(x<c):
            d+=1
            x=x*2
        print(d+n-1)    



        