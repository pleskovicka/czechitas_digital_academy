import json

# nacitam si cely text.subor ako jeden retazec a ulozim ho do premennej:
with open('alice.txt', encoding='utf-8') as file:
    text1 = file.read().lower()

# pomocou tohto kroku sa zbavim medzier a znakov pre novy riadok:
text = text1.replace(" ", "").replace("\n", "")

# vytvorim si prazdny slovnik, ktory potrebujem pre cyklus:
slovnik = dict()

# do slovniku pomocou cyklu pridavam jedinecne znaky z textu a zaroven pocitam ich vyskyt v texte ak je vacsi nez 1:
for znak in text:
    if znak in slovnik:
        slovnik[znak] += 1
    else:
        slovnik[znak] = 1   

# ulozim vysledny slovnik do suboru _.json:
with open('hw01_output.json', mode='w', encoding='utf-8') as file:
    json.dump(slovnik, file, indent=2, ensure_ascii=False, sort_keys=True)
