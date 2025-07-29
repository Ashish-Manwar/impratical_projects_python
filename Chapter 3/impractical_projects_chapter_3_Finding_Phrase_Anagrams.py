from collections import Counter

file = open("2of4brif.txt")
word_list = file.read().split()
word_list.append("i")
word_list.append("am")
user_word = input("Enter a word:")


def main():

    name = ''.join(user_word.lower().split())
    length = len(name)
    anagram_pharase = []
    count = 0
    name_dic = Counter(name)

    while count < length:
        anagram = []
        print()
        print("Choose from the following words:")
        for word in word_list:
            word_dic = Counter(word.lower())
            if word_dic <= name_dic:
                print(word)
                anagram.append(word)

        if len(anagram)==0:
            print("Choices not proper. Restart the program.")
            break
        
        user_choice = input("Choose a word from the set :")

        if user_choice in anagram:
            print(user_choice)
            anagram_pharase.append(user_choice)
            count = len(user_choice) + count
            name_dic.subtract(Counter(user_choice))
            name_dic += Counter()  # Clean up

        else:
            print("Plz choose from the listed words. Try again.")

        print(anagram_pharase)
        print("Remaining words: ",length-count )

    if count == length:
        print("Final pharase is the following :")
        print(' '.join(anagram_pharase)) 
    else:
        print("Run Again")


if __name__ == '__main__':
    main()