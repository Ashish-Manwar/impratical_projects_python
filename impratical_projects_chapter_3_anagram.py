def search(word, word_set):
    return word in word_set

def possible_combinations(word):
    letters= []
    words = []
    for letter in word:
        letters.append(letter)


    



with open("words.txt") as f:
    word_list = [line.strip().lower() for line in f]
    word_set = set(word_list)


user_word = input("Enter the word u want me find the anagram of. ")
   