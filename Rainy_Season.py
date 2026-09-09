S = input()

for i in range(3, -1, -1):
    # print("R"* i)
    if "R" * i in S:
        print(i)
        break
