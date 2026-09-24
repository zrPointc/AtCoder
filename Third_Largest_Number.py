n = int(input())
A = list(map(int, input().split()))
l = []

def a(k):
    L = []
    for i in range(k):
        L.append(A[i])
    return L

for i in range(3, n+1):
    l = a(i)
    l.sort(reverse=True)
    print(l[2])