A = list(map(int, input().split()))

average = (count(A) + min(A)) / 2

A.remove(count(A))
A.remove(min(A))

if A[0] == average:
    print("Yes")
else:
    print("No")