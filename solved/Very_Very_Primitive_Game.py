a, b, c = map(int, input().split())

# 同じ数なら先手が負け
# 1個以上の差だったら、少ないほうが負ける
if a - b >= 1:
    print("Takahashi")

elif b - a >= 1:
    print("Aoki")

elif a == b:
    if c == 0:
        print("Aoki")
    else:
        print("Takahashi")

