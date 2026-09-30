n, d = map(int, input().split())
X = list(map(int, input().split()))

people = sorted((position, number) for number, position in enumerate(X, 1))


answer = []

for index, (position, number) in enumerate(people):
    ok = True


    if index > 0:
        left_position = people[index - 1][0]
        if position - left_position < d:
            ok = False
      
    if index < n - 1:
       right_position = people[index + 1][0]
       if right_position - position < d:
           ok = False

    if ok:
       answer.append(number)

answer.sort()

print(len(answer))
if answer:
    print(*answer)

# 解説AC

# =================================================================
# 【メモ：座標上で他の全員と一定距離以上離れている人を探す】
#
# ・各人について「他のすべての人との距離が D 以上か」を判定する問題。
#
# ・全員との距離を1人ずつ調べると O(N^2) になるが、
#   座標順に並べれば「一番近い可能性がある人」は左右の隣だけ。
#
# ・そのため、座標でソートしたあと、
#   「左隣との距離」と「右隣との距離」だけ確認すればよい。
#
# ・真ん中の人：
#     左隣との距離 >= D かつ 右隣との距離 >= D
#
# ・一番左の人：
#     左隣はいないので、右隣だけ確認する。
#
# ・一番右の人：
#     右隣はいないので、左隣だけ確認する。
#
# ・注意点：
#   座標 X だけを sorted(X) すると、元の「人の番号」が分からなくなる。
#   (座標, 人番号) のペアを作ってからソートする。
#
# ・最後に求められているのは「人の番号の昇順」なので、
#   条件を満たした人の番号を最後にもう一度ソートする。
#
# 【今回の自分のコードで惜しかったところ】
# ・座標をソートして「隣同士を調べる」という方針までは合っていた。
# ・ただし左隣との距離だけで判定していたため、
#   右隣が D 未満のケースを見落としていた。
# ・さらに sorted(X) によって、元の人番号の情報を失っていた。
#
# → 「ソートして隣を見る」だけでなく、
#   「何を出力する必要があるか」「左右どちらを見る必要があるか」
#   まで整理してから実装する。
# =================================================================