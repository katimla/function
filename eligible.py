
# If user's age is less than 18 , print “not eligible “,
# else if user's age is greater than or equal to 18, print 
# “you are eligible”-

# user=int(input("enter the number"))
# def age(user):
#     if user>=18:
#         print("you are eligible")
#     elif user<=16:
#         print("not eligible")
# age(user)



# a=[1,2,3,4,5]
def num(a):
    i=0
    sum=0
    b=[]
    while i<len(a):
        sum=sum+a[i]
        b.append(sum)
    i=i+1
num([1,2,3,4,5])