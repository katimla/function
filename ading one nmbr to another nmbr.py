# list=[1,2,3,4,5]
# def num(a): 
#     i=0
#     sum=0
#     b=[]
#     while i<len(a):
#         sum=sum +a[i]
#         b.append(sum)
#         i=i+1
#     print(b)
# num([1,2,3,4,5])

# 3,5,7,9


a=[1,2,3,4,5] 
i=0
# sum=0
b=[]
while i<len(a)-1:
        # sum=sum+a[i]
        c=a[i]+a[i+1]
        b.append(c)
        i=i+1
print(b)



