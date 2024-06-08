dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
words = sentence.split()

for i in range(len(words)):
    for dicword in dictionary:
        if words[i].startswith(dicword):
                    words[i] = dicword
                    break
print(' '.join(words))