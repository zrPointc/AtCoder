X, t = map(int, input().split())

answer = X - t

if answer < 0:
    answer = 0

print(answer)