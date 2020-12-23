a=input("String ")
b=a.split(' ')
c=list(set(b))
c.sort()
print(c)
for i in c:
    e=b.count(i)
    print(i,e)
