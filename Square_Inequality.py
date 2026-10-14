a, b, c = map(int, input().split())

a **= 2
b **= 2
c **= 2

if a + b < c:
    print("Yes")
else:
    print("No")