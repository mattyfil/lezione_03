nome:str=str(input("inserisci nome "))
genere:str=str(input("inserisci genere"))
match genere:
    case "f":
        print(f"tu sei{nome} , {genere}")
    case "m":
        print(f"tu sei {nome} , {genere}")
    case _:
        print(f"errore")