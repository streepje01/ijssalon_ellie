prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" :5
}
aanbieding = prijzen["aardbei"]*0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
index = reclame_tekst.find("0")
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split()
el = ""
for woord in reclame_tekst4:
    if len(woord) >= 5:
        el += woord.upper() + "\n"
    else:
        el += woord.lower() + "\n"
print(el) 