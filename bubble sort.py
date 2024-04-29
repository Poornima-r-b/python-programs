lis=[0,1,2,3,4,5]
}c
n=len(lis)
for i in range(n):
    for j in range(n-i-1):
        if lis[j]>lis[j+1]:
            lis[j],lis[j+1]=lis[j+1],lis[j]
print(lis)