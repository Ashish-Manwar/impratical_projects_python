import sys
import string
from random import randint

def main():
    try:
        with open("2of4brif.txt") as f:
            word_list = f.read().split()
    except:
        print("Error: Could not open dictionary.")
        sys.exit(1)

    input_message = "Panel at east end of chapel slides" 
    msg = "".join(input_message.split()).lower()
    
    length = len(msg)
    
    vocab_list =[]
    """
    while count<length:
        word = random.choice(word_list)
        if len(word)> 4 and word[2].lower()==msg[count].lower() and word not in vocab_list:
            vocab_list.append(word)
            count=count+1
    """
    for letter in msg:
        word_len = randint(6,10)
        count=0
        for word in word_list:
            if len(word)==word_len and word[2]==letter and word not in vocab_list:
                vocab_list.append(word)
                break
            count = count +1
        if count==len(word_list):
            print(f"The dictonary not have {letter} at the 3 place in this dictonary.")
            break


    if len(vocab_list) < len(msg):
        print("Word list too small for full message.")
    else:
        print("Hidden message vocab:\n", *vocab_list, sep="\n")

if __name__=="__main__":
    main()