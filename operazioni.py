a:int=int(input("inserisci valore"))
b:int=int(input("inserisci valore"))
def operazioni(a:int,b:int):
    sum:int=(a+b)
    sot:int=(a-b)
    return sot,sum
print(f"{operazioni(a,b)}")
