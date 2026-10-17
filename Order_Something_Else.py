n, p, q = map(int, input().split())

D = list(map(int, input().split()))

if min(D) < q:
    print(p - q + min(D))
else:
    print(p)