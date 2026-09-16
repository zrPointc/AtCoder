n = int(input())
A = list(map(int, input().split()))
coin1, coin10, coin100 = 0, 0, 0

for i in range(n):
    if (10 - A[i] % 10) % 10 == 0:
        coin1 += 10 - A[i] % 10
    if 10 - A[i] // 10 % 10 == 0:
        coin10 += 10 - A[i] // 10 % 10

    while A[i] > 1000:
        A[i] -= 1000

    coin100 += 10 - A[i] // 100 % 10

print(coin1, coin10, coin100)
