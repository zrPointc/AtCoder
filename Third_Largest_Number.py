n = int(input())
A = list(map(int, input().split()))
l = []

def a(k):
    L = []
    smallnum = []
    for i in range(k):
        for j in range(A[i], 0, -1):
            smallnum.append(j)
        if smallnum not in A[i+1:]: 
            L.append(A[i])
    return L

for i in range(3, n+1):
    l = a(i)
    l.sort(reverse=True)
    print(l[2])