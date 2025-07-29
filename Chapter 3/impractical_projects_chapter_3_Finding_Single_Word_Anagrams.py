
file = open("2of4brif.txt")

word_list = file.read().split()

user_word = input("Enter a word:")

for word in word_list:
    if len(word) != len(user_word):
        continue
    
    elif sorted(word.lower()) == sorted(user_word.lower()):
        print(word)



