a=input("Enter the string ")
b=input("Enter the word to be removed ")
e=[]
c=a.split(' ')
d=b.split(' ')
length=len(c)
for i in c:
    if i not in d:
        e.append(i)

z=[]
for j in e:
    if j not in z:
        z.append(j)
        c1=e.count(j)
        fre=(c1/length)*100
        print(j,fre)
