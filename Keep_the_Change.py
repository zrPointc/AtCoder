n = int(input())
a = []
b = []
S = []

keep = 10000
take = 10000

for i in range(n):
    a_i, b_i, s_i = input().split()
    a.append(int(a_i))
    b.append(int(b_i))
    S.append(s_i)

    if S == "keep":
        keep -= b[i]

    take -= b[i] - a[i]

print(keep - take)