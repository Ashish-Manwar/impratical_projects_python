import nltk
from nltk.corpus import cmudict
from string import punctuation
import sys
from pprint import pprint
import json

def open_training_file(path):
    with open(path) as f:
        word_set = set(f.read().lower().replace('-'," ").split())

    return word_set

def compare_cmudict(word_set,cmu):
    missing =set()
    for word in word_set:
        word = word.lower().strip(punctuation)
        if word.endswith("'s") or word.endswith("’s"):
            word = word[:-2]
        if word not in cmu:
            missing.add(word)
    return missing

def syllabus_entry(missing):
    dic_word = dict()
    for word in missing:
        while True:
            number = input(f"How many syllabus is this {word} made of :\n")
            if number.isdigit():
                break
            else:
                print("Enter a proper number.")
        dic_word[word]=int(number)
    return dic_word

def save_missing_word(missing_word_syllabus):
    json_string = json.dumps(missing_word_syllabus)
    f = open('missing_words.json', 'w')
    f.write(json_string)
    f.close()
    print("\nFile saved as missing_words.json")



word_set = open_training_file("C:\\Users\\ashis\\OneDrive\\Desktop\\Python_learning\\Chapter 8\\train.txt")
cmu =cmudict.dict()

missing = compare_cmudict(word_set,cmu)

print(missing)

user_input = input ("\nManually build an exceptions dictionary (y/n)? \n")

if user_input =="n":
    sys.exit()

else:
    missing_word_syllabus = syllabus_entry(missing)
    pprint(missing_word_syllabus)
    save_missing_word(missing_word_syllabus)