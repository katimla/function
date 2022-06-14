
def fun(list):
    list=["p","q"]
    i=1
    b=0
    a=[]
    while i<=5:
        j=0
        while j<len(list):
            b=list[j]+str(i)
            a.append(b)
            j=j+1
        i=i+1
    print(a)
fun(list)

