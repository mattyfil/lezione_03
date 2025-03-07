nord_sud:int=int(input("inserisci valore"))
est_ovest:int=int(input("scegli valore"))
soglia=70
if nord_sud>soglia and est_ovest>soglia:
    time_ns=50
    time_es=50
    print(f"il tempo assegnato alla direzione nord-sud è",time_ns)
    print(f"il tempo assegnato alla direzione est-ovest è",time_es)
elif nord_sud>soglia:
    time_es=40
    time_ns=60
    print(f"il tempo assegnato alla direzione nord-sud è",time_ns)
    print(f"il tempo assegnato alla direzione est-ovest è",time_es)
elif est_ovest>soglia:
     time_es=60
     time_ns=40
     print(f"il tempo assegnato alla direzione nord-sud è",time_ns)
     print(f"il tempo assegnato alla direzione est-ovest è",time_es)
else:
    time_ns=(nord_sud/(nord_sud+est_ovest)*100)
    time_es=(est_ovest/(nord_sud+est_ovest)*100)
    print(f"il tempo assegnato alla direzione nord-sud è",time_ns)
    print(f"il tempo assegnato alla direzione est-ovest è",time_es)
    


