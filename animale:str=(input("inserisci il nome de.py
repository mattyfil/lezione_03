animali:str=(input("inserisci l'animale"))

mammiferi:list=["cane","gatto","cavallo","elefante","leone"]
rettili:list=["serpente","lucertola","tartaruga","coccodrillo"]
uccelli:list=["aquila","pappagallo","gufo","falco"]
pesci:list=["squalo","trota","salmone","carpa"]

match animali:
    case animali if animali in mammiferi:
        print(f"{animali} è un mammifero")
    case animali if animali in rettili:
        print(f"{animali} è un rettile")
    case animali if animali in uccelli:
        print(f"{animali} è un uccello")
    case animali if animali in pesci:
        print(f"{animali} è un pesce")
    
    case _:
        print(f"fuma meno erba")