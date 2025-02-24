start = 3
end = 100

import sys

if start <3:
    print(2,"done\n")
    sys.exit(0)
for num in range(start,end+1):
    count=0
    for i in range (2,num+1):
        if num%i==0:
            count+=1
    if count==1:
        print(num,sep=',')




