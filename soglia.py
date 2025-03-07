soglia:float=float(input("inserisci valore"))
cont=0
for cont in range(7):
    n:float=float(input("inserisci valore"))
    if n>soglia:
        print(n)
        cont+=1
    else:
        continue
