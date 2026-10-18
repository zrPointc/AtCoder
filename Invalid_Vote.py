n, m = map(int, input().split())
S = []
for i in range(n):
    S.append(input())

T = []
for j in range(m):
    T.append(input())

flag = False
count = [0] * n
icchi = [False] * n
for index, s in enumerate(S):
    for t in T:
        if s == t:
            count[index] += 1
        else:
            flag = False
            if len(s) == len(t):
                for i in range(len(s)):
                    if not s[i] == t[i] and flag:
                        flag = False
                        break
                    elif not s[i] == t[i]:
                        flag = True
                        icchi[index] = True 
                    else:
                        continue
else:
    if flag and sum(icchi) == 1:
        count[index] += 1
    elif flag and sum(icchi) > 1:
        count[icchi.index(True)] = max(0, count[icchi.index(True)] -1)
        flag = False
for i in range(n):
    print(count[i])



