a01101 = list(input())


for i in range(len(a01101)):
    if a01101[i] != "A":
        a01101[i] = "."

print(*a01101, sep="")