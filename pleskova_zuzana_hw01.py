import json

# nacitam si cely text.subor ako jeden retazec a ulozim ho do premennej:
with open('alice.txt', encoding='utf-8') as file:
    text1 = file.read().lower()

# pomocou nasledujucich dvoch krokov sa zbavim medzier a znakov pre novy riadok:
text2 = text1.replace(" ", "")
text = text2.replace("\n", "")

# vytvorim si prazdne premenne, ktore potrebujem pre nasledujuce cykly:
pocet = 0
znaky = []
slovnik = dict()

# vytvorim si zoznam jedinecnych znakov v retazci:
for znak in text:
    if znak not in znaky:
        znaky.append(znak)

# vytvorim si slovnik zo zoznamu jedinecnych znakov a dam im vsetkym hodnotu "0":
for znak in znaky:
    slovnik[znak] = 0

# spocitam opakovania/pocet jednotlivych znakov a ulozim ich do slovniku:
for znak in text:
    slovnik[znak] += 1

# ulozim vysledny slovnik do suboru _.json:
with open('hw01_output.json', mode='w', encoding='utf-8') as file:
    json.dump(slovnik, file, indent = 2, ensure_ascii = False, sort_keys = True)
