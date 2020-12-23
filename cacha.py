import random
c=''
for d in range(65,90):
    c=chr(d)
for d in range(97,123):
    c=c+chr(d)
x=''
for d in range(6):
    e=random.choice(c)
    x=x+e
print(x)
y=input("Enter the above mentioned word ")
if x==y:
    print('Matched')
else:
    print("Not matched")
