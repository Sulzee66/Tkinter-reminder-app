# def count(text):
#     counter = 1
#     for item in text.strip():
#         if item == " ":
#             counter += 1
#     print(f"There are {counter} words in the text above")
# text=input("Enter your text here: ")            
# count(text)

words = input("Type your text here: ").split(" ")
print(dict((i, words.count(i)) for i in set(words)))
