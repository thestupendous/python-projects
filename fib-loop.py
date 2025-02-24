num = 3


def fib(num):
    if num == 1:
        return 0;
    elif num == 2:
        return 1
    else:
        a,b = 0,1
        tem=0
        for i in range(num-2):
            tem=b
            b=a+b
            a=tem

        return b

print(3,fib(3))
print(4,fib(4))
print(5,fib(5))
print(6,fib(6))


        
