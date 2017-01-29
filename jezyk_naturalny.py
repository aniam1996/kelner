

x = input()                  # wpisz zdanie
zapisz=x.split()             #pod zmienną 'zapisz' podstawiamy liste slow oddzielonych przecinkiem
zamowienie = []              # tworzymy tablice 'zmowienie'


for x in zapisz:             #dodajemy slowa do tablicy 'zamowienie'
    zamowienie.append(x)



slownik = {"żurek": "zurek", "żurku": "zurek", "żurkiem": "zurek","zurek": "zurek", "zurku": "zurek", "zurkiem": "zurek",
           "rosół": "rosol", "rosołem": "rosol","rosol": "rosol", "rosolem": "rosol",
           "krupnik": "krupnik", "krupnika": "krupnik", "krupnikiem": "krupnik", "krupniku": "krupnik",
           "bigos": "bigos", "bigosu": "bigos", "bigosem": "bigos", "bigosie": "bigos",
           "placek": "placek", "placka": "placek", "plackiem": "placek", "placku": "placek",
           "schabowy": "schabowy", "schabowego": "schabowy", "schabowym": "schabowy",
           "filet": "filet", "filetu": "filet", "filetem": "filet", "filecie": "filet",
           "spaghetti": "spaghetti",
           "surówki": "surowki", "surówek": "surowki", "surówkom": "surowki","surówkami": "surowki","surówkach": "surowki","surówkę":"surowki","surówką":"surowki",
           "surowki": "surowki", "surowek": "surowki", "surowkom": "surowki","surowkami": "surowki","surowkach": "surowki","surówke":"surowki","surowka":"surowki",
           "ziemniaki": "ziemniaki", "ziemniaków": "ziemniaki", "ziemniakom": "ziemniaki","ziemniakami": "ziemniaki", "ziemniakach": "ziemniaki","ziemniakow": "ziemniaki",
           "kasza": "kasza", "kaszy": "kasza","kaszę": "kasza", "kaszą": "kasza","kasze": "kasza",
           "ryż": "ryz", "ryżu": "ryz", "ryżowi": "ryz","ryżem": "ryz","ryz": "ryz", "ryzu": "ryz", "ryzowi": "ryz","ryzem": "ryz",
           "warzywa": "warzywa", "warzyw": "warzywa", "warzywom": "warzywa", "warzywami": "warzywa", "warzywach": "warzywa",
           "dorsz": "dorsz", "dorsza": "dorsz", "dorszowi": "dorsz", "dorszem": "dorsz","dorszu": "dorsz",
           "frytki": "frytki", "frytek": "frytki", "frytkom": "frytki", "frytkami": "frytki", "frytkach": "frytki",
           "cola": "cola", "coli": "cola", "cole": "cola", "colę": "cola", "colą": "cola",
           "pepsi": "pepsi",
           "fanta": "fanta", "fanty": "fanta","fante":"fanta","fantę": "fanta", "fantą": "fanta",
           "herbata": "herbata", "herbaty": "herbata", "herbatę": "herbata","herbate": "herbata","herbatą": "herbata",
           "gazowana":"gaz","gazowaną":"gaz","gazowanej":"gaz",
           "niegazowana":"niegaz","niegazowanej":"niegaz","niegazowaną":"niegaz",
           "lemoniada": "lemoniada","lemoniady": "lemoniada", "lemoniadzie": "lemoniada", "lemoniadę": "lemoniada", "lemoniadą": "lemoniada","lemoniade":"lemoniada",
           "proponować": "propozycja", "proponuje": "propozycja", "zaproponuje": "propozycja","zaproponować": "propozycja","propozycji": "propozycja","zaproponuj":"propozycja",
           "proponowac": "propozycja","zaproponowac": "propozycja","zaproponujesz":"propozycja","propozycje":"propozycja","propozycję":"propozycja","proponujesz":"propozycja",
           "jedzenie":"jedzenie","jedzenia":"jedzenie","jedzeniu":"jedzenie","jedzeniem":"jedzenie",
           "danie":"danie","dania":"danie","dań":"danie","dan":"danie",
           "picia":"picie","picie":"picie","piciu":"picie","piciem":"picie",
           "napój":"napoj","napoj":"napoj","napoju":"napoj","napojem":"napoj"
           }

hasla = []                                  #definiujemy tablice w ktorej znajdowac sie beda slowa kluczowe
slowo=list(slownik.keys())                  #tworzymy liste w ktorej znajduja sie klucze ze slownika

for element in zamowienie:
    element=element.lower()                 #zamień wszystkie litery na małe
    if element in slowo:                    # sprawdzamy kazde slowo z zamowienia, jesli znajduje sie ono w slowniku jako klucz to dodajemy je do tablicy z haslami
            hasla.append(slownik[element])


####################################################################################################################
proponowanie=False
p=open('propozycje.txt','w')

if "propozycja" in hasla:                       #klient zażyczył sobie propozycji
    proponowanie=True
    if "picie" in hasla or "napoj" in hasla:
        p.write("napoj" +'\n')
    elif "danie" in hasla or "jedzenie" in hasla:
        p.write("jedzenie" + '\n')
    else:
        p.write("napoj" + '\n' + "jedzenie" + '\n')


p.close()


####################################################################################################################
picie = False
n=open('napoj.txt','a')

napoje = ['cola', 'pepsi', 'fanta', 'herbata', 'gaz','niegaz', 'lemoniada']

for haslo in hasla:
    if haslo in napoje:
        picie = True
        n.write(haslo + '\n')

n.close()


########################################################################################################################

jedzenie = False
j=open('jedzenie.txt','a')

danie = ['zurek', 'rosol', 'krupnik', 'bigos', 'placek', 'schabowy', 'filet', 'spaghetti', 'surowki', 'ziemniaki',
         'kasza', 'ryz', 'warzywa', 'dorsz', 'frytki']

for haslo in hasla:
    if haslo in danie:
        jedzenie = True
        j.write(haslo + '\n')


j.close()
#######################################################################################################################

podsumowanie={"Propozycja":proponowanie, "Napoj":picie, "Danie":jedzenie}

zapisz=["%s=%s" % (k, v) for k, v in podsumowanie.items()]

pods=open('podsumowanie.txt','w')
for i in zapisz:
    pods.write(i + '\n')
pods.close()

