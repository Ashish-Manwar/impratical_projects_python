from itertools import permutations

word = "tmvoordle"

word_list = permutations(word, len(word))
word_set =[]

for words in word_list:
    dummy = ''.join(words)
    if dummy not in word_set:
        word_set.append(dummy)


