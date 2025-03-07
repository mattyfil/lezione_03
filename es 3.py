sum=0
cont=0
for cont in range(5):
    n:int=int(input("inserisci valore"))
    if n>0:
        sum+=n
        cont+=1
else:
    print(f"{sum}")