blueball_a, blueball_b, redball_c, time_d = map(int,input().split())

n = 0
if blueball_b >= redball_c * time_d:
    print(-1)
else:
    while blueball_a +  blueball_b*n > redball_c * n * time_d:
        n += 1
    print(n)

# 解説AC