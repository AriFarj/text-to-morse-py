import pandas as pd
characters = pd.read_csv("morse.csv")
morse_letters = {row.character: row.code for (index, row) in characters.iterrows()}

word = input("Enter a word\n").upper()
morse_translate = [morse_letters[character] for character in word]
full_word = " ".join(morse_translate)
print(full_word)