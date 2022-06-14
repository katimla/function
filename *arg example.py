def adder(*num):
    sum=0
    for n in num:
        sum=sum+n
    print("sum:",sum)
adder(3,4,5)
adder(1,2,6)
adder(8,9,2)
def my_child(*kids):
    print("youngest child is",kids[2])
my_child("emil","katim","pinu")