list_of_names = []
with open("./Input/Names/invited_names.txt") as names:
    for name in names.readlines():
        final_name = name.replace("\n", "")
        list_of_names.append(final_name)

for name_on_letter in list_of_names:
    with open("./Input/Letters/starting_letter.txt") as base_letter:
        base_letter = base_letter.read()
        final_letter = base_letter.replace("[name]", name_on_letter)
    with open(f"./Output/ReadyToSend/letter_for_{name_on_letter}.txt", mode="w") as completed_letter:
        completed_letter.write(final_letter)
