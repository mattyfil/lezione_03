a:int=int(input("inserisci"))
b:int=int(input("inserisci "))


def sottrazione (a:int,b:int):
    sott:int=0
    match sott:
        case sott if b>a:
            sott=b-a
        case sott if a>b:
            sott=a-b
            return sott
        

        

print(f"{sottrazione(b,a)}")
print(f"{sottrazione(a,b)}")
