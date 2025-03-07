#esercizio 5 match

nome:str=(input("inserisci nome    "))
eta:int=(input("inserisci età    "))
ruolo:str=(input("inserisci ruolo    "))
azienda:dict={"ruolo":ruolo,"nome":nome,"età":eta}


match azienda:

    case azienda if ruolo=="admin":
        print(f"{ruolo}hai tutte le funzionalità,signor{nome}\n,dall'eta di{eta}")
    case azienda if ruolo=="moderatore":
       print(f"{ruolo}puoi gestire contenuti ma non li puoi modificare,signor{nome}\n,dall'eta di{eta}")
    case azienda if eta>=18:
        print(f"{nome }hai accesso a tutti i servizi standard\n{eta}")
    case azienda if eta<18:
        print(f"{nome}hai accesso limitati ai servizi")
    case azienda if ruolo=="ospite":
        print(f"{ruolo}hai accesso ristretto signor{nome} \n,di età{eta}")
    case _:
        print(f"ruolo non riconosciuto")
