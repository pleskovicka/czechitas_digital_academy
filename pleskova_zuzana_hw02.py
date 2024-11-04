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

# RIESENIE PODLA PRVYCH KOMENTAROV:
'''
.Na řádku 35 zavádíš proměnou new_keys, kterou na řádku 40 uložíš do proměnné keys. Nebála bych se, pojmenovat ji keys rovnou 
na začátku a toto přeuložení už nemusíš dělat.
.Na řádku 48 zůstal zapomenutý print(keys) – do terminálu se nemá nic vypisovat.
.Líbí se mi, že sis zvlášť načetla první řádek jako hlavičku a data do druhé proměnné.
.Doporučila bych ale do bloku with open zařadit jen řádek 34 a řádky 42 a 43, které načítají data ze souboru a dále pokračovat 
novým blokem kódu bez odsazení – soubor se tak po načtení zavře. To vyžaduje úpravu proměnné values. Ideální by bylo ji definovat 
jako prázdný seznam před otevřením souboru a jednotlivé řádky do ní načíst pomocí metody append.
.Takto budeš mít dva seznamy keys a values a můžeš je spojit do slovníku row_dict pomocí funkce zip. Bude nutné definovat opět 
for cyklus, který bude procházet seznam values a brát z něj jednotlivé seznamy value po jednom a k němu připojovat odpovídající 
klíče ze seznamu keys. Syntax je dict(zip(keys, value). Jednotlivé slovníky pak můžeš postupně připojovat do prázdného seznamu 
netflix_movies zase pomocí append. 
.Pořadí sloupců podle zadání by mělo být title, directors, cast, genres, decade. Máš to přehozené, 
protože jak python prochází kódem, 
tak si bere údaje z originálního pořadí sloupců, které je seřazené jinak, než potřebujeme my. To by se dalo vyřešit předdefinováním 
struktury slovníku new_dict na řádku 55 – tedy nezavedeš jen prázdný slovník, ale rozepíšeš jednotlivé názvy klíčů a k nim odpovídající předpokládané 
hodnoty ( např. "title": ""). Pořadí zůstane zachované, tak jak zadáš ty a nemusíš tedy ani na řádku 64 spouštět nový for cyklus. 
Slovník poté plníš hodnotami pomocí kódu od řádku 56.
.Vícenásobné podmínky můžeš řešit pomocí elif.
.Líbí se mi podmínka, která řeší prázdný slovník pro sloupce directors,…
.Správně jsi vyřešila dekádu letopočtu na řádku 66, ale zůstaly tam jedny závorky navíc. Pokud bys výsledek dělení nechtěla 
přetypovat znovu na int, můžeš místo dělení použít dělení beze zbytku //, které vrací celé číslo.
'''


import json

# Nacitam prvy riadok s nazvami stlpcov do premennej COL_NAMES a ostatne riadky do zoznamu VALUES:
values = []
with open("netflix_titles.tsv", encoding="utf-8") as input_file:
    col_names = input_file.readline().lower().strip().split("\t")
    for line in input_file:
        values.append(line.strip().split("\t"))

# Ulozim si nove kluce pozadovane v zadani ulohy:
keys = []
for key in col_names:
    new_key = key.replace("director", "directors").replace(
        "primarytitle", "title")
    keys.append(new_key)

# vytvorim z novych klucov a riadkov povodneho dokumentu zoznam slovnikov:
netflix_movies = []
for list in values:
    row_dict = dict(zip(col_names, list))
    netflix_movies.append(row_dict)

# upravim podla zadania format "stlpcov" a vypocitam dekadu:
keys1 = ["title"]  # tieto ako retazce
keys2 = ["directors", "cast", "genres"]  # tieto stlpce chcem ako zoznamy
movies = []
for dictionary in netflix_movies:
    new_dict = {"title": "", "directors": [],
                "cast": [], "genres": [], "decade": int}
    for key, value in dictionary.items():
        if key in keys1:
            new_dict[key] = value
        elif key in keys2:
            new_dict[key] = value.split(",")
            if value == "":
                new_dict[key] = []
        elif key == "startyear":
            dec = int(value)//10*10
            new_dict["decade"] = dec
    movies.append(new_dict)

# ulozim vysledny zoznam slovnikov do suboru _.json:
with open('hw02_output.json', mode='w', encoding='utf-8') as file:
    json.dump(movies, file, indent=2, ensure_ascii=False, sort_keys=False)
