# with open('text.txt', 'r') as f:
#     # f.seek(12)
#     # f.write(" for the rich ones")
#     # with open('text.txt','r') as f:
#     data=f.read()
#     print(data)
import random as rd

characters=['0','1']
r_chars=''.join(rd.choice(characters) for i in range (0,4))
conv_r_chars=int(r_chars,2)
print(conv_r_chars)
