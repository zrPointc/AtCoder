onaka, buy, eat = map(int, input().split())

if buy >= eat:
    print("delicious")
elif eat - buy <= onaka:
    print("safe")
else:
    print("dangerous")
