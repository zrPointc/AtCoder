S = input()
answer = ""
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        answer = "Bad"
        break

if not answer:
    answer = "Good"

print(answer)