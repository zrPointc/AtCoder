n = int(input())
answer = []
if n % 2 == 0:
    for i in range(n):
        if i == (n//2 - 1) or i == (n//2):
            answer.append("=")
        else:
            answer.append("-")

else:
    for i in range(n):
        if i == (n//2):
            answer.append("=")
        else:
            answer.append("-")

print(*answer, sep="")