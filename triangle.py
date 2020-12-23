n=int(input("Enter the limit "))
for i in range(0,n):
    for j in range(i,n-1):
        print("",end=(''))
    for k in range(1,i+1):
        print("*",end=(''))
    print('\n')

'''for i in range(0,n):
    for k in range(0,i+1):
        print("",end=(''))
    for j in range(i,n-2):
        print("*",end=(""))
    print('\n')          
'''

