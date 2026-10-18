n, p, q = map(int, input().split())
D = list(map(int, input().split()))

if q + min(D) < p:
    print(q + min(D))
else:
    print(p)