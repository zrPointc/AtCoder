n = int(input())
answer = 1

def div2(num):
    count = 0
    while num % 2 == 0:
        num //= 2
        count += 1

    return count

max = 0

for i in range(1, n+1):

    if max < div2(i):
        max = div2(i)
        answer = i

print(answer)

# 解説AC