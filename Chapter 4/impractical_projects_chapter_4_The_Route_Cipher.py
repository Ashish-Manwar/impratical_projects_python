from itertools import permutations

#==============================================================================
# USER INPUT:

# the string to be decrypted (type or paste between triple-quotes):
ciphertext = """REST TRANSPORT YOU GODWIN VILLAGE ROANOKE WITH ARE YOUR IS JUST
SUPPLIES FREE SNOW HEADING TO GONE TO SOUTH FILLER
"""

# the number of columns believed to be in the transposition matrix:
COLS = 4

# the number of rows believed to be in the transposition matrix:
ROWS = 5

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#==============================================================================

cipherlist = list(ciphertext.split())

matrix_raw =[]

for i in range(COLS):
    cols_temp =[]
    for j in range(ROWS):
        cols_temp.append(cipherlist[i*ROWS+j])
    matrix_raw.append(cols_temp)

print(matrix_raw)


key = [1,2,3,4]

key_possibilities = list(permutations(key))

print(len(key_possibilities))

for i in range(len(key_possibilities)):
    key_list = key_possibilities[i]

    matrix = []
    for col in key_list:
        matrix.append(matrix_raw[col-1])
        
    print(matrix)
    

    