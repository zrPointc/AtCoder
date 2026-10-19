S1 = input()
S2 = input()

if (S1[0] == "A" and S2[1] == "D") or (S1[0] == "D" and S2[1] == "A") or (S1[1] == "A" and S2[0] == "D") or (S1[1] == "D" and S2[0] == "A"):
    print("No")
else:
    print("Yes")