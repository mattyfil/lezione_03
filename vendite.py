nome:str=str(input("inserisci il nome"))
vendita:int=int(input("inserisci valore "))
max_nome:str=nome
max_vendite:int=vendita
min_vendite:int=vendita
min_nome:str=nome
cont:int=0
while cont<20:
    cont+=1
    new_nome:str=str(input("inserisci nome"))
    new_vendita:int=int(input("inserisci valore"))
    if new_vendita>max_vendite:
        max_vendite=new_vendita
        max_nome=new_nome
    elif new_vendita<min_vendite:
        min_vendite=new_vendita
        min_nome=new_nome
    else:
        continue
print(f"{max_vendite,max_nome}")
print(f"{min_nome,min_vendite}")