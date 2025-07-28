file = open("words.txt")
pali_list=[]
for word in file:
    if len(word.strip())>1 and word.strip()==word.strip()[::-1]:
        pali_list.append(word.strip())
    

print(pali_list)