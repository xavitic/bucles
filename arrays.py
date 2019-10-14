a = [1,2,3,4,5]

print(a[1])
pos = 2
a[0] = a[0]*2
a[1] = a[1]*2
a[pos] = a[pos]*2
a[3] = a[3]*2
a[4] = a[4]*2

posicio = 0
while posicio < 5:
    a[posicio]= 2*a[posicio]
    posicio = posicio + 1

print(a[0])


