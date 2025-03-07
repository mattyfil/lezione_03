n:int=int(input("inserisci il numero di bambini"))
match n:
    case 1:
        print(f"Congratulazioni")
    case 2:
        print(f"Wow gemelli")
    case 3:
        print(f"Wow! tre!")
    case 4:
        print(f"Mamma mia quattro")
    case 5:
        print(f"incredibili 5")
    case _:
        print(f"non ci credo {n} bambini")