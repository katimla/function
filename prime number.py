
def num(a):
    i=0
    while i<len(a):
        j=1
        count=0
        while j<=a[i]:
                if a[i]%j==0:
                        count=count+1
                j=j+1
        if count==2:
                print(a[i],"prime")
        else:
                print(a[i],"not prime")
        i=i+1
num([1,7,8])





# prime number 1 to 100

# def add():
#         i=2
#         while i<=100:
#                 j=2
#                 count=0
#                 while j<i:
#                         if i%j==0:
#                                 count=count+1
#                         j=j+1
#                 if count==0:
#                         print(i,"prime")
#                 i=i+1
# add()

