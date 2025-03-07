binario:int=int(input("inserisci un numero in binario"))
c=0
decimale=0
for x in binario:
    c+=1
    match binario:
        case binario if binario[-1]==1:
                decimale=(2*(binario[:-1]**c))+
        case binario if binario[-1]==0:
              decimale=(2*(binario[:-1]**c))
        case binario if binario[-2]
        
              

                    
print(f" in decimale è {decimale}")

