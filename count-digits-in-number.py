number = 8292131

#string way
number=str(number)
for ch in number:
    print(ch)

print()

number = 8292131
out=[]
while number>0 :
    dig=number%10
    out.append(dig)
    number//=10

for i in range(len(out)-1,-1,-1):
    print(out[i])

