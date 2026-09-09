n = int(input())
A = list(map(int,input().split()))

answer = []

for a in A:
    if a % 2 == 0:
        answer.append(a)

print(*answer)