def reverse(num):
    negative=False
    if(num<0):
        num = -num
        negative=True

    rev=0
    while num>0:
        dig = num%10
        rev = (rev * 10) + dig
        num//=10

    if negative:
        return -rev
    else:
        return rev

print(reverse(1234))
print(reverse(-1234))
