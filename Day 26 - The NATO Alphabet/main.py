import pandas as pd

# Creating Nato Dictionary from CSV
df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}


# Generating final result to return NATO Alphabet
def generating_nato():
    input_word = input("Please enter a word: ")
    try:
        result_list = [nato_dict[letter.upper()] for letter in input_word]
    except KeyError:
        print("Sorry, please enter only letters in the alphabet please.")
        generating_nato()
    else:
        print(result_list)


generating_nato()
