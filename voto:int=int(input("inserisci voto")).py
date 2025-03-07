voto:int=int(input("inserisci voto"))
match voto:
    case voto if voto >=106 or voto==110:
        print(f"il tuo voto è 4.0")
    case voto if voto >=101 or voto==105:
        print(f"il tuo voto è 3.7")
    case voto if voto >=96 or voto==100:
        print(f"il tuo voto è 3.3")
    case voto if voto >=91 or voto==95:
        print(f"il tuo voto è 3.0")
    case voto if voto >=86 or voto==90:
        print(f"il tuo voto è 2.7")
    case voto if voto >=81 or voto==85:
        print(f"il tuo voto è 2.3")
    case voto if voto >=76 or voto==80:
        print(f"il tuo voto è 2.0")
    case voto if voto >=70 or voto==75:
        print(f"il tuo voto è 1.7")
    case voto if voto >=66 or voto==69:
        print(f"il tuo voto è 1.0")
    case _:
        print(f"voto non valido")
