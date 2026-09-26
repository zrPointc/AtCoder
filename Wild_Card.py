n = int(input())
S = input()
T = input()
answer = ""
for i in range(n):
    if S[i] == T[i] or T[i] == "*":
        continue
    else:
        answer = "No"
        break

if not answer:
    print("Yes")
else:
    print(answer)