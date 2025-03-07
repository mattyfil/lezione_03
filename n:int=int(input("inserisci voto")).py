n:int=int(input("inserisci voto"))



match n:
        case n if n >=90 and n <=100:
            print(f"hai preso A")
        case n if n<90 and n>=80:
            print(f"hai preso B")
        case n  if n<80 and n>=70:
            print(f"hai preso C")
        case n if n<70 and n>=60:
            print(f"hai preso D")
        case _:
          print(f"non hai passato l'esame")




