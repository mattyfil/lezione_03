alien_color:str=str(input("scegli tra verde giallo rosso \n"))
match alien_color:
    case "verde":
        print(f"hai guadagnato 5 punti")
    case "rosso" :
        print(f"hai guadagnato 15punti")
    case _ :
        (f"hai guadagnato 10 punti ")

   

        