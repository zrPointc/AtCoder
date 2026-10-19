import statistics

n = int(input())

C = list(map(int, input().split()))
m = statistics.mode(C)
# print(C.count(m))
print(len(C) - C.count(m))