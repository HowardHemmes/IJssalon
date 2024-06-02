def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print
    
def fooi_pp(bedrag,personen):
        bedrag_pp = bedrag / personen
        bedrag_pp_uit = f"Het bedrag per persoon is {bedrag_pp:.2f} euro"

def onderstreep(tekst=""):
    uit = []
    uit.append (tekst)
    uit.append (len(tekst) * "=")
    return uit

def som(invoer):
    waarde = 0
    for key, value in invoer.items():
        waarde = waarde + value
    
    return waarde