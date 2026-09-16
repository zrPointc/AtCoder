r, g, b = map(int,input().split())
c = input()

if c == "Red":
    if g <= b:
        print(g)
    else:
        print(b)
elif c == "Green":
    if r <= b:
        print(r)
    else:
        print(b)
else:
    if r <= g:
        print(r)
    else:
        print(g)