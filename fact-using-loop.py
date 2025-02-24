def fact(num):
    f=1
    for i in range(1,num+1):
        f  *= i
    return f


print(3,fact(3))
print(5,fact(5))
print(7,fact(7))
print(9,fact(9))

