S = input()
answer = []
for i in range(len(S)):
    if i != len(S)-1:
        answer.append(S[i])
        answer.append("o")
    else:
        answer.append(S[i])

print(*answer, sep="")