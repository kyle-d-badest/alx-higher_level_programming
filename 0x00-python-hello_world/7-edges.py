#!/usr/bin/python3
word = "Holberton"
# first two letters goes here
print((f"First 3 letters: {word[0:-6]}").format(word=word))
#last two letters goes here
print((f"Last 2 letters: {word[7:]}").format(word=word))
#midle word goes here
print((f"Middle word: {word[1:-1]}").format(word=word))
