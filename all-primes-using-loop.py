start = 3
end = 100


plist=[]

nums = { i:True for i in range (2,end+1) }

for i in range (2,end+1,2):
    for j in range(i+1,end+1):
        if j%i==0:
    
