once, money, count = map(int, input().split())

if once * count <= money:
    print(count)
else:
    print(money // once)
    