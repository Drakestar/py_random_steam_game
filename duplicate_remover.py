file = open("games.txt", "r")
no_duplicates = []
for x in file.readlines():
    if x not in no_duplicates:
        no_duplicates.append(x)
file.close()
file = open("games.txt", "w")
for x in no_duplicates:
    file.write(x)
file.close()

