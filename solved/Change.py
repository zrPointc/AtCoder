n = int(input())
A = list(map(str, input().split()))
coin1, coin10, coin100 = 0, 0, 0
calc = 0
for i in range(n):
    if A[i] != "1":
        calc = 1000 * (int(A[i][0]) + 1) - int(A[i])
    else:
        calc = 999

    coin1 += calc % 10
    coin10 += calc % 100 // 10
    coin100 += (calc % 1000) // 100

print(coin1, coin10, coin100)
