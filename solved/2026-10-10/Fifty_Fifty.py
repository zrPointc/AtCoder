S = input()

fifty1 = False
fifty2 = False

if len(set(S)) == 2:
    fifty1 = True

if S.count(S[1]) == 2:
    fifty2 = True

if fifty1 and fifty2:
    print("Yes")
else:
    print("No")