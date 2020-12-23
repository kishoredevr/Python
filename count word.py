a=input("Enter the string ")
e=[]
b=a.split(' ')
for i in b:
    if i not in e:
        e.append(i)
        c=a.count(i)
        print(c,i)
