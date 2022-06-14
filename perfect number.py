

n=int(input("enter the number"))
def perfect(n):
    i=1
    sum=0
    while i<=n//2:
        if n%i==0:
            sum=sum+i
        i=i+1
    if sum==n:
        print(n,"is a perfect number")
    else:
        print(n,"is not a perfect number")
perfect(n)





# def perfect(n):
#     i=1
#     while i<=n:
#         sum=0
#         j=1
#         while j<i:
#             if i%j==0:
#                 sum+=j
#             j+=1
#         if sum==i:
#             print(i,"is  perfect number ")
#         i=i+1
# perfect(1000)

