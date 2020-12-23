def amstrong(n):
    a=n
    b=[]
    c=0
    f=0
    while(n!=0):
        b.append(n%10)
        f=f+1
        n=n//10
    for i in range(0,len(b),1):
        c=c+(b[i]**f)
    if(c==a):
        print(a,"Is an amstrong no")
    else:
        print(a,"Is not an amstrong no")
