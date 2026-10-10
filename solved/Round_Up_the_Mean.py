a, b = map(int, input().split())

average = (a + b) / 2

average *= 10

if average % 10 != 0:
    average += average % 10

print(int(average // 10))