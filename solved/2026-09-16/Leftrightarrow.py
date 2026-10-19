S = input()
ans = ""
while ans == "":
  if S[0] != "<":
    ans = "No"
    break
  if S[-1] != ">":
    ans = "No"
    break

  if S[1:-1] != "=" * (len(S)-2) or S[1] != "=":
    ans = "No"
    break

  ans = "Yes"
    
print(ans)