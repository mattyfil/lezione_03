t:str="testa"
c:str="croce"
t=t.upper()
c=c.upper()
count_t=0
count_c=0
for x in range(8):
    x:str=str(input("inserisci risultato della moneta "))
    match x:
        case x if x=="testa" or x==t:
            count_t+=1
        case x if x=="croce" or x==c:
            count_c+=1
       
perc_t=(count_t/8)*100
perc_c=(count_c/8)*100

print(f"la percentuale dei testa e croce sono {perc_c}% e {perc_t}%")