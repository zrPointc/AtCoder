n = int(input())
S = list(input().split())
ans = ""
s2 = ["a", "b", "c"]
s3 = ["d", "e", "f"]
s4 = ["g", "h", "i"]
s5 = ["j", "k", "l"]
s6 = ["m", "n", "o"]
s7 = ["p", "q", "r", "s"]
s8 = ["t", "u", "v"]
s9 = ["w", "x", "y", "z"]

for i in range(n):
    if S[i][0] in s2:
        ans += "2"
    if S[i][0] in s3:
        ans += "3"
    if S[i][0] in s4:
        ans += "4"
    if S[i][0] in s5:
        ans += "5"
    if S[i][0] in s6:
        ans += "6"
    if S[i][0] in s7:
        ans += "7"
    if S[i][0] in s8:
        ans += "8"
    if S[i][0] in s9:
        ans += "9"

print(ans)