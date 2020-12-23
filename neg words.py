a=input("Enter the sentance ")
b=input("Enter the words to be removed ")
c=a.split(' ')
d=b.split(' ')
e=[]
for f in c:
    if f in d:
        e.append(f)
print(e)
d=[]
for i in e:
    if i not in d:
        d.append(i)
        f=e.count(i)
        print((f/len(c))*100,i,f)
        #h[i]=((f/len(c))*100)
       
