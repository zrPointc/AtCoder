n, a, b, = map(int,input().split())
total = 0
for i in range(n+1):
    digit_sum = sum(map(int, str(i)))
    if a <= digit_sum <= b:
        total += i

print(total)

# 各桁の取り出しかた
sum_digit = 0
while N > 0:
    sum_digit += N % 10
    N //= 10