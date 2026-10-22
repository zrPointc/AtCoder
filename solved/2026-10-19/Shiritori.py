# Shiritori

# 入力される単語の個数
n = int(input())

# n 個の単語をリストに保存する
words = []
for _ in range(n):
    words.append(input())

# 最初は「しりとりが成立している」と仮定する
is_shiritori = True

# set は同じ値を 1 つにまとめる。
# 要素数が違えば、同じ単語が 2 回以上登場している。
if len(words) != len(set(words)):
    is_shiritori = False

# 前の単語の最後の文字と、次の単語の最初の文字を順に比べる
for i in range(n - 1):
    previous_word = words[i]
    next_word = words[i + 1]

    # つながっていなければ、しりとりは成立しない
    if previous_word[-1] != next_word[0]:
        is_shiritori = False
        break

# 全ての条件を満たしていれば Yes、そうでなければ No を出力する
if is_shiritori:
    print("Yes")
else:
    print("No")
