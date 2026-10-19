shop_n = int(input())
apx = []
for i in range(shop_n):
    apx.append(list(map(int, input().split())))


minutes = 0
apx = sorted(apx)

price = 100000000000

for i in range(shop_n):
    if apx[i][0] < apx[i][2]:
        if price > apx[i][1]:
            price = apx[i][1]

if price == 100000000000:
    price = -1


print(price)

# 解説AC