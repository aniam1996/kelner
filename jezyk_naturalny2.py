

x = input()                  # wpisz zdanie
zapisz=x.split()             #pod zmienną 'zapisz' podstawiamy liste slow oddzielonych przecinkiem
zamowienie = []              # tworzymy tablice 'zmowienie'


for x in zapisz:             #dodajemy slowa do tablicy 'zamowienie'
    zamowienie.append(x)



slownik = {"tak":"tak","poprosze":"tak","poproszę":"tak","poprosimy":"tak","dobrze":"tak","spróbuję":"tak","sprobuje":"tak","spróbuje":"tak",
           "rachunek":"rachunek","zaplacic":"rachunek", "zapłacić":"rachunek",
           }

hasla = []                                  #definiujemy tablice w ktorej znajdowac sie beda slowa kluczowe
slowo=list(slownik.keys())                  #tworzymy liste w ktorej znajduja sie klucze ze slownika

for element in zamowienie:
    element=element.lower()                 #zamień wszystkie litery na małe
    if element in slowo:                    # sprawdzamy kazde slowo z zamowienia, jesli znajduje sie ono w slowniku jako klucz to dodajemy je do tablicy z haslami
            hasla.append(slownik[element])


####################################################################################################################

potw=open('potwierdzenie.txt','w')

if "rachunek" in hasla:
    potw.write("rachunek"+'\n')
elif "tak" in hasla:
    potw.write("tak"+'\n')
else:
    potw.write("nie"+'\n')

potw.close()