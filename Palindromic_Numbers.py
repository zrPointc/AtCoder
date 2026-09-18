a, b = map(int, input().split())
answer = 0
for i in range(a, b+1):
    l = []
    for j in range(5):
        l.append(str(i)[j])
    if l[0] == l[4] and l[1] == l[3]:
        answer += 1
print(answer)