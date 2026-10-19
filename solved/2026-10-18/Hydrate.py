blueball_a, blueball_b, redball_c, time_d = map(int,input().split())

n = 0
if blueball_b >= redball_c * time_d:
    print(-1)
else:
    while blueball_a +  blueball_b*n > redball_c * n * time_d:
        n += 1
    print(n)

# 解説AC

# ---------------  Hydrate.py  ---------------
# AtCoder の問題「Hydrate」の解答例（コメント付き）

# ① 入力を取得
blueball_a, blueball_b, redball_c, time_d = map(int, input().split())

# ② 1 回の追加で青玉が増える速さ
#     1 秒あたりに赤玉が減る速さ * 時間
#     （つまり 1 回の追加で赤玉が減る個数）
red_per_round = redball_c * time_d

# ③ 青玉が増える速度が赤玉が減る速度を上回る／等しい場合
#     → 追いつかないので答えは -1
if blueball_b >= red_per_round:
    print(-1)
else:
    # ④ 追いつくのに必要な最小回数を計算
    #     n * (red_per_round - blueball_b) >= blueball_a
    #     → n = ceil( blueball_a / (red_per_round - blueball_b) )
    denom = red_per_round - blueball_b  # 正の整数
    n = (blueball_a + denom - 1) // denom  # 切り上げ除算
    print(n)
