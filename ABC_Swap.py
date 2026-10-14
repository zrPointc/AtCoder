x, y, z = map(int, input().split())

altbox = y
y = x 
x = altbox

altbox = z
z = x
x = altbox

print(x, y, z)