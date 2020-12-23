a=input("String ")
b=int(input("Limit "))
for i in range(0,b+b,2):
    print(a[i],end=(''))
print("\n")
for j in range(1,b+b,2):
    print(a[j],end=(''))
for j in range(b+b,len(a)):
    print(a[j],end=(''))
