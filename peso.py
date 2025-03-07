peso:float=float(input("inserisci il peso"))
altezza:float=float(input("inserisci l'altezza"))
mci:float=peso/(altezza**2)
match mci:
    case mci if mci>40:
        print(f"devi metterti a dieta")
    case mci if mci<40 and mci>=30:
        print(f"situazione migliorabile")
    case mci if mci <30 and mci >=20:
        print(f"situazione ottimale")
    case _:
        print(f"valore non valido")
