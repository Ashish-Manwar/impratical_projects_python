import math
import itertools
#------------------------------------------------------------------------------
# USER INPUT:

# the string to be decrypted (paste between quotes):
ciphertext = """LTSRS OETEI EADET NETEH DOTER EEUCO SVRHR VRNRS UDRHS AEFHT ES

"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#------------------------------------------------------------------------------

ciphertext_list =ciphertext.split()
ciphertext_join = "".join(ciphertext_list)
print(ciphertext_join)

length = len(ciphertext_join)
n= math.ceil(length/2)
row1= ciphertext_join[:n].lower()
row2= ciphertext_join[n:].lower()

plaintext=[]

for r1,r2 in itertools.zip_longest(row1,row2):
    plaintext.append(r1)
    plaintext.append(r2)

print("".join(plaintext))


