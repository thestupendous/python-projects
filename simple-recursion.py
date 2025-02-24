def rec_add(num):
    if num<1: return 0
    else:
        return num + rec_add(num-1)


print(rec_add(10))
print(rec_add(5))
print(rec_add(20))
