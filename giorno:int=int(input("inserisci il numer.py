giorno:int=int(input("inserisci il numero del giorno   "))
mese:int=int(input("inserisci il numero del mese  "))

data=(giorno,mese)
match data:
    case data if giorno==1 and mese==1:
        print(f" è capodanno")                  
    case data if giorno==14 and mese==2:
        print(f"è san valentino")
    case data if giorno==2 and mese==6:
        print(f"è la festa della reppublica")
    case data if giorno==15 and mese==8:
        print(f"è ferragosto")
    case date if giorno==31 and mese==10:
        print(f"è hallowin")
    case date if giorno==25 and mese==12:
        print(f"è natale")
    case _:
        print(f"non ci sono festività")

