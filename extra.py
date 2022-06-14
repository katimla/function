# num=1
# def function():
#     num=3
#     print(num)
# function()
# print(num)

# num=1
# def function():
#     global num
#     num=num+3
#     print(num)
# function()
# print(num)

# def test(x=1,y=2):
#     x=x+y
#     y+=1
#     print(x,y)
# test(2,1)



# def sum(a,b):
#     add=(a+b)
#     print(add)
# sum(20,30)

# def sum(a,b):
#     c=(a-b)
#     print(c)
# sum(20,30)

# def hero(a,b):
#     print(a+b)
# hero()

# def dub(x,y):
#     a=x-y
#     print(a)

# x=7
# def sum(a,b):
#     y=x+a
#     print(y)
# sum(7,16)
# print(x)
# print(a)

# def sum(a,b):
#     x=a*b
#     return(x)
#     print(x)
# print(sum(6,4))

# def add(a,b):
#     return(a+b)
# def sub (c,d):
#     print(add(3,9))
#     return(c-d)
# print(sub(7,14))

# def add(a,b):
#     return(a*b)
# def sub(c,d):
#     print(add(3,9))
#     return(c-d)
# print(sub(7,14))

# def add(a,b):
#     return(a+b)
# def sub(c,d):
#     print(add(5,5))
#     return(c,d)
# def num(f,g):
#     print(sub(10,5))
#     return(f*g)
# print(num(3,10))


# def employee(name,salary=20000):
#     print(name,"your salary is:-",salary)

# employee("kartik",30000)
# employee("deepak")





# x=4
# y=x+x
# def m(p,q):
#     i=0
#     while i<=2:
#         print(y)
#         i=i+1
#     print(x)
#     return i
# print(m(2,4))





# def x():
#     y=7+a
# x=()
# print(y)
# print(x)


# from re import X


# def sum (a,b):
#     x=a+b
#     return x
# print(sum(5,6))

# def add(x,y):
#     print(x+y)
#     return(x)
# print(add(4,9))



# a=[2,3,4,5]
# i=0
# even=0
# odd=0
# while i<len(a):
#     if i%2==0:
#         print("even")
#     else:
#         print("odd")


# def my(list):
#     i=-1
#     a=[]
#     while i>=-len(list):
#         a.append(list[i])
#         i=i-1
#     return a
# print(my([1,2,3,4,5,6]))


a=[1,3,5,7,4,6,9,12,4,10]
# o/p=[[1,3],[5,7]]
i=0
d=[]
while i<len(a):
    b=[]
    b.append(a[i])
    d.append(b)
    
    i+=1
print(d)

    
        