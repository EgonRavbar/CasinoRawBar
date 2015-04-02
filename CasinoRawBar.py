from random import randint
skrivno = randint(-10, 10)
print("Pozdravljeni, bi zeleli preizkusiti sreco?")
stevilo = 0
while stevilo != skrivno:
    a = raw_input("Uganite, katero stevilo imam v mislih.")
    stevilo = int(a)
    if stevilo == skrivno:
        print("Cestitamo, ste pravi bralec misli!")
    else:
        if stevilo > skrivno:
            print("Poizkusite ponovno. Izbrali ste previsoko stevilo.")
        else:
            print("Poizkusite ponovno. Izbrali ste prenizko stevilo.")
print("Hvala sodelovanje!")