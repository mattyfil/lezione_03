soglia:int=int(input("inserisci soglia"))
cont=1
while cont<7:
    cont+=1
    n:int=int(input("inserisci valore"))
    if n>soglia:
        print(f"{n}")
    else:
        continue