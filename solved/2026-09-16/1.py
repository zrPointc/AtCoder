x = int(input())

bank = 100
years = 1
while True:
    bank += bank // 100
    if bank >= x:
        print(years)
        break
    
    years += 1