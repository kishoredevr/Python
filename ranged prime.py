a=int(input("Start="))
b=int(input("End="))
for i in range(a,b+1):
    f=0
    for j in range(2,i//2):
        if i%j==0:
            f=1
            break
    if f==0:
         print(i)
