from algemene_functies import mijn_functie_2 

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) met smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    bedrag = totaal * (btw / 100)
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    return max(mijn_lijst), min(mijn_lijst)

def gemiddelde(mijn_lijst):
    bedrag = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {bedrag} euro."

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])

