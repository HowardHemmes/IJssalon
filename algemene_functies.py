def mijn_functie_1(keuze):
    mijn_tabel = {
        2 : 4,
        4 : 16,
        10 : 100,
        12 : 144
    }
    uitvoer = mijn_tabel[keuze]
    return uitvoer

def mijn_functie_2(keuze2):
    mijn_tabel2 = {
        "12,3" : "[15, 9, 36, 4]",
        "12,2" : "[14, 10, 24, 6]",
        "10,5" : "[15, 5, 50, 2]",
        "100,20" : "[120, 80, 2000, 5]"
    }
    uitvoer2 = mijn_tabel2[keuze2]
    return uitvoer2

print(mijn_functie_1(4))
print(mijn_functie_2("12,2"))