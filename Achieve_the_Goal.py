# 平均点を求める式で、iの値を大きくしていく全探索（？）
n, k, m = map(int, input().split())
A = list(map(int, input().split()))
ans = -1
for i in range(k+1):
    if m <= (sum(A) + i) / n:
        ans = i
        break

print(ans)


"""
平均点×科目数で合計点を求めて、既得点を引く
n, k, m = map(int, input().split())
A = list(map(int, input().split()))
ans = (n * m)-sum(A)
if ans < 0:
    print(0)
elif ans > k:
    print(-1)
else:
    print(ans)
"""