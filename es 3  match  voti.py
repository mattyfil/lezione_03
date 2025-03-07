n:int=int(input("inserisci numero"))
match n:
            case n if n==10:
                print(f"eccelente")
            case n if n==8 or n==9:
             print(f"molto buono")
            case n if n==7 or n==6:
             print(f"sufficiente")
            case n if n==5 or n==4:
                print(f"insufficiente")
            case n if n>=1 or n==3:
                print(f"gravemente insufficiente")
            case _:
                print(f"voto non valido")