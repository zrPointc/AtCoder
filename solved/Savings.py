n = int(input())
day = 1
piggy_bank = 0
while True:
    piggy_bank += day

    if piggy_bank >= n:
        print(day)
        break
    
    day += 1