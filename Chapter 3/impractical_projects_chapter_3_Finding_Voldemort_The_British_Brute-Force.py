from itertools import permutations

def main():
    name = "tmvoordle"

    volde_per = permutations(name)
    perms = []
    for letters in volde_per:
        perms.append("".join(letters))
    volde_per_set = set(perms)
    print("Total Premuatations=", len(volde_per_set))


    file = open("2of4brif.txt")
    word_list = file.read().split()

    cv_map_word_list = cv_map(word_list)
    print(len(cv_map_word_list))

def cv_map(word_list):

    vowels ="aeiou"
    cv_map_word_list =[]

    for word in word_list:
        cv_map_word = ""
        for letter in word:
            if letter in vowels:
                cv_map_word=cv_map_word + "v"
            else:
                cv_map_word=cv_map_word + "c"
        cv_map_word_list.append(cv_map_word)
        
    
    return cv_map_word_list








if __name__=="__main__":
    main()
    


