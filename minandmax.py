a=input("Enter the string ")
b=a.split(' ')
c=b[0]
for i in b:
    if len(c)<len(i):
        c=i
print(c +"is greater")
       
