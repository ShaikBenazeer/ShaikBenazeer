a=[-1,-2,3,-6,-3,3]
j=0
for i in range(len(a)):
    if a[i]<0:
        if i!=j:
           t=a[j]
           a[j]=a[i]
           a[i]=t
        j=+1
print(a)
