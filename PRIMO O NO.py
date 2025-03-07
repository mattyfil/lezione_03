n:float=float(input("inserisci valore"))
è_primo=True
if n<2 :
    è_primo=False
else:
    div=2
    while True:
        if div<n:
            if n%div!=0:
                div+=1
        elif n%div==0:
            è_primo=True
        else:
            è_primo=False

        
            
