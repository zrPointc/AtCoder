n, d = map(int, input().split())

X = list(map(int, input().split()))
X = sorted(X)
print(X)
count = 0
answer = []
for i in range(1,n):
    if abs(X[i] - X[i-1]) >= d:
        print(X[i],X[i-1],abs(X[i] - X[i-1]),d)
        count += 1 
        answer.append(i)  



print(count)
if count:
   print(*answer)

