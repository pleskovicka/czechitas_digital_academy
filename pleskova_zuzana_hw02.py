'''
ZADÁNÍ:

Napište skript, který přečte obsah souboru netflix_titles.tsv obsahující filmy a převede je do seznamu
slovníků, který uloží do JSON souboru hw02_output.json. Z každého řádku vás budou zajímat pouze
následující údaje:
PRIMARYTITLE (název)
DIRECTOR (seznam režisérů)
CAST (seznam herců)
GENRES (seznam žánrů)
STARTYEAR (rok vydání)

Tyto údaje převedete do slovníku s následujícími klíči a hodnotami:
<"title": str, "directors": list, "cast": list, "genres": list, "decade": int> 

Protože formát TSV neumožňuje reprezentovat seznam, jsou herci, režiséři a žánry zadáni jako jeden řetězec
a jednotlivé hodnoty jsou oddělené čárkami. Ve formátu JSON použijte pro větší přehlednost seznam, aby
bylo například vidět, kolik herců nebo režisérů v seznamu je.

Může se stát, že film neobsahuje údaj o režisérech nebo hercích, ostatní jsou vždy uvedené. Pokud není
uveden žádný režisér nebo herec, daná položka musí být prázdný seznam [], nikoli seznam s řetězcem
o nulové délce [""].

Dekáda je vždy první rok desetiletí, např. rok 1987 patří do dekády 1980 a rok 2017 do dekády 2010.
'''

import json

netflix_movies = []
with open("netflix_titles.tsv", encoding="utf-8") as input_file:
    # Nacitam prvy riadok s nazvami stlpcov -> kluce slovnikov a zaroven niektore znenie opravim podla zadania:
    old_keys = input_file.readline().lower().strip().split("\t")
    new_keys = []
    for key in old_keys:
        new_key = key.replace("director", "directors").replace(
            "primarytitle", "title")
        new_keys.append(new_key)
    keys = new_keys
    # Nacitam zvysne riadky a ulozim ich do slovnikov s novymi klucmi:
    for line in input_file:
        values = line.strip().split("\t")
        row_dict = dict()
        for no in range(len(keys)):
            row_dict[keys[no]] = values[no]
        netflix_movies.append(row_dict)
print(keys)

# vytvorim (nove) kluce, ktore ma zaujimaju a podla nich vyberiem zo suboru len to, 
# co do slovnikov potrebujem:
keys1 = ["title"]  # tieto ako retazce
keys2 = ["directors", "cast", "genres"]  # tieto stpce chcem ako zoznamy
movies = []
for dc in netflix_movies:
    new_dict = dict()
    for key, value in dc.items():
        if key in keys1:
            new_dict[key] = value
        if key in keys2:
            new_dict[key] = value.split(",")
            if value == "":
                new_dict[key] = []
    # schvalne zacinam novy cyklus, pretoze chcem aby kluc dekady bol na konci slovniku:
    for key, value in dc.items():
        if key == "startyear":
            dec = int((int(value)/10))*10
            new_dict["decade"] = dec

    movies.append(new_dict)

# ulozim vysledny slovnik do suboru _.json:
with open('hw02_output.json', mode='w', encoding='utf-8') as file:
    json.dump(movies, file, indent=2, ensure_ascii=False, sort_keys=False)
