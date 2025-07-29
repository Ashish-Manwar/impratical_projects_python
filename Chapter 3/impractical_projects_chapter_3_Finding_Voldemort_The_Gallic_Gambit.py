from itertools import permutations

word = "vodle"

word_list = permutations(word, len(word))
count =0

for words in word_list:
    print(''.join(words))
    count=count+1

print(count)




