import string

def main():
    text = input("Input text for bar chart:\n").lower()

    # Step 1: Remove punctuation and spaces
    cleaned_text = ''
    for char in text:
        if char not in string.punctuation and not char.isspace():
            cleaned_text += char

    # Step 2: Count letters
    words = dict()
    for char in cleaned_text:
        words[char] = words.get(char, 0) + 1

    # Step 3: Build and print bar chart
    print("\nBar Chart:")
    for letter in sorted(words):
        print(letter, ":" , "*" * words[letter])  # e.g., a: ***

if __name__ == "__main__":
    main()
