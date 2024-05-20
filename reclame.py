from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    aanbieding_prijs = prijs - prijs*korting
    aanbieding_prijs_str = str(f"{aanbieding_prijs:.2f}").replace('.',',')
    reclame_tekst = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {aanbieding_prijs_str} euro."
    uitvoer = reclame_tekst
    return uitvoer

def inkomsten_totaal(inkomsten,btw):
    totaal = sum(inkomsten)
    totaal_str = str(f"{totaal:.2f}").replace('.',',')
    bedrag = totaal * btw
    bedrag_str = str(f"{bedrag:.2f}").replace('.',',')
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal_str} euro, waarover {bedrag_str} euro btw betaald dient te worden."
    return uitvoer

def gemiddelde(mijn_lijst2):
    aantal_waarden = len(mijn_lijst2)
    som = sum(mijn_lijst2)
    gemiddelde = som / aantal_waarden
    bedrag = str(f"{gemiddelde:.2f}").replace('.',',')
    uitvoer = f"De gemiddelde inkomsten deze week zijn {bedrag} euro."
    return uitvoer

def hoog_en_laag(invoer_lijst):
    hoog = max(invoer_lijst)
    laag = min(invoer_lijst)
    uitvoer = hoog,laag
    return uitvoer

def meervoudig(invoer_lijst):
    uitvoer = hoog_en_laag(invoer_lijst)
    return uitvoer

def combinatie(invoer_lijst_2)
    korte_lijst=meervoudig(invoer_lijst_2)
    mf2=mijn_functie_2(korte_lijst)
    return mf2
    
mijn_lijst=[220, 430, 125, 160, 205, 90, 345]
mijn_invoerlijst=[10,5,3,2,1,2,9]
print(aanbieding_1("aardbei", 4, 0.1))
print(inkomsten_totaal(mijn_lijst,0.09))
print(gemiddelde(mijn_lijst))
print(meervoudig(mijn_invoerlijst))