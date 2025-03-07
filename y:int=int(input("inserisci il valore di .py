y:float=float(input("inserisci il valore di y  "))
x:float=float(input("inserisci il valore di x "))
coordinate=(x,y)
match coordinate:
    case coordinate if x==0 and y==0:
        print(f" sta all'origine")
    case coordinate if y==0:
        print(f"si trova sull'asse x")
    case coordinate if x==0:
        print(f"si trova sull'asse y")
    case coordinate if x>0 and y>0:
        print(f"si trova nel primo quadrante")
    case coordinate if x<0 and y<0:
        print(f"si trova nel secondo quadrante")
    case coordinate if x>0 and y<0:
        print(f"si trova nel quarto quadrante")
    case coordinate if x<0 and y>0:
        print(f"si trova nel terzo quadrante")
    case _:
        print(f"inserisci 2 numeri con un senso logico")
    
