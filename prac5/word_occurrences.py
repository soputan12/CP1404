user_text = input("Text: ")
word_count = {}
words = user_text.split()
for i in words:
    count = word_count.get(i, 0)
    word_count[i] = count + 1
words = list(word_count.keys())
words.sort()
for word in words:
    length = len(word)
    print(f"{word} : {word_count[word]}")