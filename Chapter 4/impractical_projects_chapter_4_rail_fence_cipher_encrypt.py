#------------------------------------------------------------------------------
# USER INPUT:

# the string to be encrypted (paste between quotes):
plaintext = """Let us cross over the river and rest under the shade of the trees
"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#------------------------------------------------------------------------------


def main():
    plaintext_list=plaintext.split()
    length = len(plaintext_list)

    row1 = []
    row2 = []

    for i in range(length):
        if i%2==0:
            row1.append(plaintext_list[i])
        else:
            row2.append(plaintext_list[i])

    print(row1)
    print(row2)

    msg_cipher_list=row1 + row2
    msg_cipher="".join(msg_cipher_list) 
    count =1
    for word in msg_cipher:
        if count%5==0:
            print(word.upper(),end="")
            print(" ",end="")
        else:
            print(word.upper(),end="")
        count=count +1

    

if __name__=="__main__":
    main()