def operate(num1,op,num2):
    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='/':
        return num1/num2
    elif op=='*':
        return num1*num2
aa = input()

input_list = aa.split()
print(input_list)
# num1,num2,op
counter = 0
ans = 0
op = ''

ans = int(input_list[0])
for i in range(1,len(input_list),2):
    op=input_list[i]
    num2=int(input_list[i+1])
    temp = operate(ans,op,num2)
    ans = temp
    print("isme      : ",temp)
    print("updated : ",ans)

print("result : ",ans)
