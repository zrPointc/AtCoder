p = int(input())
total = 0
count = 0
def bikkuri(n):
    calc = 1
    for i in range(1, n+1):
        calc *= i
    return calc

while p > 0:
    for i in range(10, 0, -1):
        if p >= bikkuri(i):
            c = p // bikkuri(i)
            count += c
            p -= bikkuri(i) * c
            print(i,p, bikkuri(i), c)


print(count)

# あまりから前の効果の枚数、pからあまり引いたりする
# 2から順に割っていってあまり出せる？