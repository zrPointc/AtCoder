n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = ""
for i in range(m):
    if B[i] in A:
        A.remove(B[i])
        continue
    else:
        break
else:
    answer = "Yes"

if not answer:
    answer = "No"
print(answer)