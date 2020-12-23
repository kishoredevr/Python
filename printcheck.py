f=0
n=int(input("Enter the limit "))
while(f==0):
    s=input("Enter your string ")
    if (n==len(s)):
        for i in range(0,len(s),2):
            print(s[1],end=(''))
        print('\n')
        for i in range(1,len(s),2):
            print(s[1],end=(''))
        f=1
    else:
        print("Enter the correct string of length ",n)
        f=0
        
