#esercizio 8.12
condimenti:list=[]
def fare_panino(*args:None)->None:
    while True:
        a:str=str(input("che condimento vuoi, sennò scrivi quit    "))
        condimenti.append(a)
        if a=="quit":
            condimenti.pop(-1)
            break
    return condimenti

print(f"nel panino vuoi",fare_panino(condimenti))
    
