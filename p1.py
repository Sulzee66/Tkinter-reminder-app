sentence= input("Input your sentence:\n")
vowels=['a','e','i','o','u']
number =0

for i in sentence:
    if i in vowels:
        number+=1

print("There are ",number," vowels in this sentence")