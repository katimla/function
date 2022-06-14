# a="school"
def num(a):
    i=0
    c=0
    c1=0
    c2=0
    c3=0
    c4=0
    while i<len(a):
        if "s" in a[i]:
            c=c+1
        elif "c" in a[i]:
            c1=c1+1
        elif "h" in a[i]:
            c2=c2+1
        elif "o" in a[i]:
            c3=c3+1
        elif "l" in a[i]:
            c4=c4+1
        i=i+1
    print("s:",c)
    print("c:",c1)
    print("h:",c2)
    print("o:",c3)
    print("l:",c4)
num("school")
