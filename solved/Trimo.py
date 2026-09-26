n = int(input())
S = input()

for _ in range(n):
    if len(S) > 0:
        if S[0] == "o":
            S = S.lstrip("o")
            # S.lstrip("o") と書いていた

print(S)