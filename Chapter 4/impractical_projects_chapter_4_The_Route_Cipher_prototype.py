ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19" 
cipherlist = list(ciphertext.split())       

# 🔹 Step 3: Set matrix parameters
COLS = 4
ROWS = 5
key = '-1 2 -3 4'

matrix_raw =[]

for i in range(COLS):
    cols_temp =[]
    for j in range(ROWS):
        cols_temp.append(cipherlist[i*ROWS+j])
    matrix_raw.append(cols_temp)

key_list = list(key.split())

for i in range(COLS):
    key_list[i] = int(key_list[i])

matrix = []
for i in range(COLS):
    if key_list[i] < 0:
        matrix.append(matrix_raw[i][::-1])
    else:
        matrix.append(matrix_raw[i])

msg =[]

for i in range(ROWS):
    for j in range(COLS):
        msg.append(matrix[j][i])
        
print("".join(msg))

        




    