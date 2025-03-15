a=10
b=20
def swap(a,b):
    a=a^b
    b=a^b
    a=a^b
    return a,b
print(swap(a,b))
