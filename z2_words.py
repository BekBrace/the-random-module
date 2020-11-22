# mini-project : pluck a user generated number of words from the words.txt file
import random
print(">>> Random Word Finder <<<")
print("\nUsing a 170K English word text file I can pick any word ata random.\n")
words_number = int(input("\nHow many words shall I choose >>>"))
with open("your file path goes here ... ", "rt") as f:
    words = f.readlines()
words = [w.rstrip() for w in words]

print('----------------------')
for w in random.sample(words, words_number):
    print(w)
print('----------------------')
