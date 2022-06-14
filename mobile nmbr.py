def add():
    a=[1,2,3,0,4,8,0,9,8]
    b=""
    c=""
    d="-"
    i=0
    while i<len(a):
        if i<3:
            b=b+str(a[i])
        if i>=3 and i<=5:
            c=c+str(a[i])
        if i>=6:
            d=d+str(a[i])
        i=i+1
    y="("+b+")"
    print(y+c+d)
add()






# def my():
#     user=int(input("enter the number"))
#     i=0
#     s=0
#     while i<user:
#         user1=int(input("enter the number"))
#         if user1 %3==0:
#             s=s+user1
#         i=i+1
#     print(s)
# my()



def my(n,n1):
    if n>0 and n1>0:
        i=0
        s=0
        while i<=n1:
            m=i*n
            if m==n1 or m<n1:
                s=s+m
            i=i+1
        print(s)
    else:
        print("invalid")
    
n=int(input("enter the number"))
n1=int(input("enter the number"))
my(n,n1)