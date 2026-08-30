S = input()
upper = False
lower = False
different = False
for i in range(0, len(S)):
    if S[i].isupper():
        upper = True
        
    if S[i].islower():
        lower = True

if len(set(S)) == len(S):
    different = True

if upper and lower and different:
    print("Yes")
else:
    print("No")