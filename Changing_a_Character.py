n, k = map(int, input().split())

S = input()

for i, s in enumerate(S):
    if k == i + 1:
        S = S[:i] + S[i].lower() + S[i + 1:]

print(S)

# また解きたい問題