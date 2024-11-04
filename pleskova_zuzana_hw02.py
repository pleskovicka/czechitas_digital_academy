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

# RIESENIE PODLA DALSICH KOMENTAROV:
'''
Pokud bys chtěla celý kód zeštíhlit, nemusíš na začátku vůbec řešit hlavičku vytvářet slovník pro všechny sloupce z tabulky. 
Můžeš načíst data až od druhého řádku jako seznam sezanmů, a poté rovnou přejít k definování slovníku new_dict, pojmenovat klíče,
tak jak je potřeba (title, directors,...) a hodnoty definovat pomocí číselného indexu sloupce, ve kterém se nachází. 
Což předpokládá, že se na data podíváš a víš, že např primarytitle je na indexu [2]. Můžeš taky definovat vlastní funkci, 
třeba na přpočet dekády nebo seznam u directors a na tomto místě ji zavolat.
'''
import json


# definujem si funkciu DECADE na premenu roku na dekadu:
def decade(year):
    return int(year)//10*10

    
# nacitam subor filmov z netflixu do zoznamu zoznamov VALUES:
values = []
with open("netflix_titles.tsv", encoding="utf-8") as input_file:
    input_file.readline()  # preskocim prvy riadok
    for line in input_file:
        values.append(line.strip().split("\t"))

# vytvorim slovniky s pozadovanymi klucmi a nahradim prazdne retazce praznym zoznamom, a vsetko ulozim do premennej VALUES:
movies = []
for value in values:
    new_dict = {"title": value[2],
                "directors": value[15].split(","),
                "cast": value[16].split(","),
                "genres": value[8].split(","),
                "decade": decade(value[5])}
    for key, value in new_dict.items():
        if value == [""]:
            new_dict[key] = []
    movies.append(new_dict)

# ulozim vysledny zoznam slovnikov do suboru _.json:
with open('hw02_output.json', mode='w', encoding='utf-8') as file:
    json.dump(movies, file, indent=2, ensure_ascii=False, sort_keys=False)
