import time
def is_palindrome(word):
    return word == word[::-1]

def search(word, word_set):
    return word in word_set

start_time =time.time()
# Load all words into a list and a set
with open("words.txt") as f:
    word_list = [line.strip().lower() for line in f]
    word_set = set(word_list)

# Check for palingrams
for word in word_list:
    w_len = len(word)
    if w_len > 2:
        for i in range(1, w_len):  # avoid empty prefix/suffix
            prefix = word[:i]
            suffix = word[i:]

            # Type 1: palindromic prefix + reversed real word at end
            if is_palindrome(prefix) and search(suffix[::-1], word_set):
                print(suffix[::-1],word, i)

            # Type 2: palindromic suffix + reversed real word at start
            elif is_palindrome(suffix) and search(prefix[::-1], word_set):
                print(word,prefix[::-1], i)
end_time =time.time()
print("Runtime for this program was {} seconds.".format(end_time - start_time))
