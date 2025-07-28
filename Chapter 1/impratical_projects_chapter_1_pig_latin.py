"""Pig Latin converter script for single English words."""

def main():
    """Take a word as input and convert it to Pig Latin."""
    word = input(
        "Enter a word in English to give u the pig latin version of it.\n "
        ).strip().lower()

    if not word:  
        print("No input!")
    elif not word.isalpha():
        print("Give only letters")
    elif word[0] in "aeiou":
        print(word+"way")
    elif len(word) > 1:
        print(word[1:]+word[0]+"ay")
    else:
        print(word+"ay")


if __name__=="__main__":
    main()
