file = open('grossgames.txt', 'r')
game_list = []
temp_string = ""
spell_count = 0
quote_count = 0
badstrings=['friendlyURL', 'global_achievements', 'friendly_name', 'availStatLinks', 'stats', 'has_adult_content']
line = file.readlines()
line = line[0]
for x in line:
    # Start spelling name
    if spell_count == 0:
        if 'n' in x:
            spell_count += 1
    elif spell_count == 1:
        if 'a' in x:
            spell_count += 1
    elif spell_count == 2:
        if 'm' in x:
            spell_count += 1
    elif spell_count == 3:
        if 'e' in x:
            spell_count += 1
    # A "name" has been found
    elif spell_count == 4:
        if '\"' in x:
            quote_count += 1
        elif quote_count == 2:
            temp_string += x
        elif quote_count == 3:
            spell_count = 0
            quote_count = 0
            if temp_string not in badstrings:
                temp_string = temp_string.replace('\\u2122', '')
                game_list.append(temp_string)
            temp_string = ""


print(game_list)
file.close()
file = open("games.txt", 'w')
for x in game_list:
    file.write(x)
    file.write("\n")
file.close()
