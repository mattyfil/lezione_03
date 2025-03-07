n:int=int(input("inserisci numero"))
match n:
    case n if n%2==0:
        print(f" {n} è pari")
    case _:
        print(f"{n} è disparo")