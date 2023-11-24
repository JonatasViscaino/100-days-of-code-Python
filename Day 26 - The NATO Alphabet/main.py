import pandas as pd

# Creating Nato Dictionary from CSV
df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# Generating final result to return NATO Alphabet
input_word = input("Please enter a word: ")
result_list = [nato_dict[letter.upper()] for letter in input_word]
print(result_list)