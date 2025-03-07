animale:str=(input("inserisci l'animale   "))
habitat_1:str=(input("inserisci habitat   "))
mammiferi:list=["cane","gatto","cavallo","elefante","leone","balena","delfino"]
rettili:list=["serpente","lucertola","tartaruga","coccodrillo"]
uccelli:list=["aquila","pappagallo","gufo","falco","cigno","anatra","tacchino"]
pesci:list=["squalo","trota","salmone","carpa"]
animali:list=[mammiferi,rettili,pesci,uccelli]

habitat:list=["aria","acqua","terra"]

match animale:
    case animale if animale in mammiferi [0:4]and habitat_1=="terra":
        print(f"{animale} vive nella {habitat_1} fa parte della categoria {animali[0]}")
    case animale if animale in mammiferi [5:7] and habitat_1 ==habitat[1]:
        print(f"{animale} vive nel {habitat[1]} e fa parte della categoria {animali[0]}")
    case animale if animale in rettili and habitat_1==habitat[2]:
        print(f"{animale} vive sulla{habitat[2]} ferma e fa parte della categoria {rettili}")
    case animale if animale in rettili and habitat_1==habitat[1] or habitat_1==habitat[2]:
        print(f"{animale} vive sull  {habitat[1]} e sulla {habitat[2]} ferma e fa parte della categoria {rettili}")
    case animale if animale in uccelli and habitat_1==habitat[0]:
        print(f"{animale} vive nel {habitat[0]}  e fa parte della categoria {uccelli}")
    case animale if animale in uccelli and habitat_1==habitat[0] or habitat_1==habitat[1]:
        print(f"{animale} vive nel {habitat[1]} e fa parte della categoria {uccelli}")
    case animale if animale in uccelli and habitat_1==habitat[2]:
        print(f"{animale} vive nel {habitat[2]} ferma e fa parte della categoria {uccelli}")
    case animale if animale in pesci:
        print(f"{animale} vive in {habitat[1]}  e fa parte della categoria {pesci}")
    
    case _:
        print(f"fuma di meno")

        





