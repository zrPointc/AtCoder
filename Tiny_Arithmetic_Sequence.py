A = list(map(int, input().split()))

average = (max(A) + min(A)) / 2

A.remove(max(A))
A.remove(min(A))

if A[0] == average:
    print("Yes")
else:
    print("No")