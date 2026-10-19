Sx, Sy, Gx, Gy = map(int, input().split())

# x = Sx + t * (Gx - Sx)
# y = Sy + t * (-Gx - Sy)

# x軸は、y = 0なので、
# 0 = Sy - t * (Gx + Sy)
# t = Sy / (Sy + Gy)

# t を x に代入 
# x = Sx + (Sy / (Sy + Gy)) * (Gx - Sx)
x = Sx + (Gx - Sx) * Sy / (Sy + Gy) 

print(x)

# 解説AC
# -------------- Billiards.py -------------
# 出発点 S = (Sx, Sy)、壁で反射する前の目標点 G = (Gx, Gy) を受け取る
Sx, Sy, Gx, Gy = map(int, input().split())

# 反射を考える代わりに、G を x 軸について反転した点 (Gx, -Gy) へ
# まっすぐ進むと考える。この直線と x 軸の交点が答えになる。
#
# S から反転後の G までの縦方向の距離は Sy + Gy。
# x 軸に着くまでに下がる距離は Sy なので、直線全体のうち
# Sy / (Sy + Gy) だけ進んだ位置に交点がある。
ratio = Sy / (Sy + Gy)

# x 座標も同じ割合だけ Sx から Gx へ進めばよい。
answer_x = Sx + (Gx - Sx) * ratio

print(answer_x)

# この解法は計算量 O(1)、追加メモリ O(1)。
# 点を反転して直線との交点を求める方法が、シミュレーションをせずに済む最も簡潔な解き方。
