oggetti:list=[]
for x in range(3):
    oggetti.append(input("inserisci oggetto"))
  
    print(oggetti)
match oggetti:
        case oggetti if oggetti==["penna","matita","quaderno"]:
            print(f"lista materiale scolatisco")
        case oggetti if oggetti==["pane","latte","uova"]:
            print(f"lista alimenti da mangiare")
        case oggetti if oggetti==["sedia","tavolo","armadio"]:
            print(f"mobili")
        case oggetti if oggetti==["telefono","computer","tablet"]:
            print(f"roba informatica")
        case _:
            print(f"lista non valida")
    