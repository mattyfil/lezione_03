n:int=int(input("inserisci valore"))
fat:int=1
i:int=1
if n>0:
    print(f"{n}")
    while i<n:
        i+=1
        fat=fat*i
else:
    print(f"devi mettere un numero positivo idiota")
print(f"{fat}")