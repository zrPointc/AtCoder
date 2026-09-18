A, B = map(int, input().split())

for x in range(1, 1100):
    tax8 = int(x * 0.08)
    tax10 = int(x * 0.10)

    if tax8 == A and tax10 == B:
        print(x)
        exit()

print(-1)

# 解説AC