pari:int=0
dispari:int=0
cont:int=0
while cont <10:
    cont+=1
    n:int=int(input("inserisci valore"))
    if n%2==0:
        pari+=1
    else:
        dispari+=1
print(f"{pari},{dispari}")
