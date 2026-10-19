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

# 店の数を入力
shop_count = int(input())

# 購入できる商品の最安値
# None は「まだ購入できる店が見つかっていない」ことを表す
minimum_price = None

for _ in range(shop_count):
    # arrival_time: 店に到着するまでの時間
    # price: 商品の価格
    # sold_out_time: 商品が売り切れるまでの時間
    arrival_time, price, sold_out_time = map(int, input().split())

    # 到着時刻が売り切れる時刻より前なら購入できる
    if arrival_time < sold_out_time:
        # 最初に見つけた商品、または現在の最安値より安い商品なら更新
        if minimum_price is None or price < minimum_price:
            minimum_price = price

# 購入できる店がなければ -1
if minimum_price is None:
    print(-1)
else:
    print(minimum_price)