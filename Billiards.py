Sx, Sy, Gx, Gy = map(int, input().split())

# x = Sx + t * (Gx - Sx)
# y = Sy + t * (-Gx - Sy)

# x軸は、y = 0なので、
# 0 = Sy - t * (Gx + Sy)
# t = Sy / (Sy + Gy)

# t を x に代入 
# x = Sx + (Sy / (Sy + Gy)) * (Gx - Sx)
x = Sx + (Gx - Sx) * Sy / (Sy + Gy) 

print(x)

# 解説AC