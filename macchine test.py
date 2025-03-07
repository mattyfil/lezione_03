i=0
scelta_vera=0
scelta_falsa=0

for i in range (10):
    car:str=str(input("inserisci marca e modello della macchina"))


    if car=="nissan" :
    
        print(f"prevedo che la tua macchina sia della")
        print(f"la tua macchina è una {car}")
        scelta_vera+=1
    



    else:
    
        print(f" prevedo non sia quella migliore\prevedo falso")
        print(f"non è la macchina prevista  {car}")
        scelta_falsa+=+1


print(scelta_falsa,scelta_vera)
