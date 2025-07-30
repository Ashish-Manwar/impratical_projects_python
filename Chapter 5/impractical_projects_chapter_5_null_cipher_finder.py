"""Decode a null cipher based on number of letters after punctuation marks."""

import string
import sys


def load_file(path):
    with open(path) as f:
        return f.read().strip()
    

def solve_null_cipher(msg,lookahead):
    for i in range(1,lookahead+1):
        plain =""
        count=0
        found_first = False
        for ch in msg :
            if ch in string.punctuation:
                count=0
                found_first = True
            elif found_first:
                count = count +1
            if count==i:
                plain = plain + ch
        print(f"Offset {i}: {plain}" )


def main():
    filename = input("Enter the file path: ")
    try:
        loaded_msg = load_file(filename)
    except IOError as e:
        print(f"The file as thrown error {e}")
        sys.exit(1)

    print(f"\nOriginal message:\n{loaded_msg}\n")
    msg = "".join(loaded_msg.split())

    
    while True:
        lookahead = (input("How many letters to look after punctuation? "))
        if lookahead.isdigit():
            lookahead = int(lookahead)
            break
        else:
            print("Please enter a number.")

    """
    length = len(msg)
    punc_loc = []

    for i in range(length):
        letter = msg[i]
        if letter in string.punctuation:
            punc_loc.append(i)

    punc_loc_1 = [number-1 for number in punc_loc]
    common = (list(set(punc_loc) & set(punc_loc_1)))

    for i in common:
        punc_loc.remove(i)


    for i in punc_loc:
        if i+3<length:
            print(msg[i+3],end="")
    print()
    """

    solve_null_cipher(msg,lookahead)


if __name__=="__main__":
    main()
