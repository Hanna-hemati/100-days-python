PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.read()

with open("./Input/Letters/starting_letter.docx") as letter_file:
    letter_n = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_n.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{name}.docx", mode="r") as complete_letter:
            complete_letter.write((letter_n))

