frase:str=str(input("inserisci la frase che vuoi   "))
spazi:int=frase.count(" ")
x:int=len(frase)

match frase:
    case frase if frase[-1]=="?" and (x-spazi)%2==0:
        print(f"SI! {frase}")
    case frase if frase[-1]=="?" and (x-spazi)%2!=0:
        print(f"NO!{frase}")
    case frase if frase[-1]=="!":
        print(f"WOW{frase}")
    case _:
        print(f" Tu dici {frase}")

