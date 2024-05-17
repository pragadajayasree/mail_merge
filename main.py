with open("./Input/Names/invited_names.txt") as data:
    names = data.readlines()
with open("./Input/Letters/starting_letter.txt") as data:
    text = data.read()
replace_name = "[name]"
for name in names:
    new = name.strip()
    new_text = text.replace(replace_name, new)
    with open(f"./Output/ReadyToSend/letter_{new}.txt", mode="w") as data:
        data.write(new_text)



