import random as rd
import string as st
def generate_password(length):
    #characters = ['0','1','2','3','4','5','6','7','8','9']
    characters = st.digits + st.ascii_letters
    password = ''.join(rd.choice(characters) for i in range(length)) #length is the no of characters of the password to be generated
    return password
password = generate_password(8)
print(password)
# from random import randint as rand

# word = []
# while(len(word)<8):
#     word.append(str(rand(0,9)))
# print("".join(word))
