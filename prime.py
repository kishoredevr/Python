a=int(input("Number="))
f=0
for i in range (2,a//2):
    if a%i==0:
        f=1
        break
if f==0:
    print("Prime")
else:
    print("Not a prime")
