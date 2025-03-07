n:int=int(input("inserisci numero"))
match n:
    case 1:
        print(f"è il mese di gennaio")
    case 2:
        print(f"è il mese di febbraio")
    case 3:
        print(f"è il mese di marzo")
    case 4:
        print(f"è il mese di aprile")
    case 5:
        print(f"è il mese di maggio")
    case 6:
        print(f"è il mese di giugno")
    case 7:
        print(f"è il mese di luglio")
    case 8:
        print(f"è il mese di agosto")
    case 9:
        print(f"è il mese di settembre")
    case 10:
        print(f"è il mese di ottobre")
    case 1:
        print(f"è il mese di novembre")
    case 12:
        print(f"è il mese di dicembre")
    case _:
        print("non esiste il mese")
