from helper import som

def presenteer(Mijn_dict, totaal):
    
    for sleutel, waarde in Mijn_dict.items():
        print(f"{sleutel} : {waarde} euro")
        
    print(26 * "=")
    
    tot = som(Mijn_dict)
    print(f"totaal : {tot} euro")