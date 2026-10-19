n = int(input())
W = []
for i in range(n):
    W.append(input())

flag = True
if len(W) != len(set(W)):
    flag = False
for i in range(n-1):
    if W[i][-1] == W[i+1][0]:
        continue
    else:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")

# 解説AC