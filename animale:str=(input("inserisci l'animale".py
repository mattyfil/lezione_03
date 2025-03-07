animale:str=(input("inserisci l'animale   "))

mammiferi:list=["cane","gatto","cavallo","elefante","leone","balena","delfino"]
rettili:list=["serpente","lucertola","tartaruga","coccodrillo"]
uccelli:list=["aquila","pappagallo","gufo","falco","cigno","anatra","tacchino"]
pesci:list=["squalo","trota","salmone","carpa"]
animali:list=[mammiferi,rettili,pesci,uccelli]

habitat:list=["aria","acqua","terra"]

match animale:
    case animale if animale in mammiferi and animale in (mammiferi[0:4]):
        print(f"{animale} vive nella {habitat[2]}")
    case animale if animale in mammiferi and animale in (mammiferi[5:7]):
        print(f"{animale} vive nel {habitat[1]}")
    case animale if animale in rettili and animale in (rettili[0:2]):
        print(f"{animale} vive sulla{habitat[2]} ferma")
    case animale if animale in rettili and animale in (rettili[2:4]):
        print(f"{animale} vive sull  {habitat[1]} e sulla {habitat[2]} ferma")
    case animale if animale in uccelli and animale in (uccelli[0:3]):
        print(f"{animale} vive nel {habitat[0]}")
    case animale if animale in uccelli and animale in (uccelli[4:6]):
        print(f"{animale} vive nel {habitat[1]}")
    case animale if animale in uccelli and animale in uccelli[7]:
        print(f"{animale} vive nel {habitat[2]}")
    case animale if animale in pesci:
        print(f"{animale} vive in {habitat[1]}")
    
    case _:
        print(f"fuma di meno")

        





