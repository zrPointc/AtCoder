n = int(input())

A = list(map(int, input().split()))

A = A[(n//2):]

print(sum(A))