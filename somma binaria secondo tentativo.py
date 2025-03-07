a:int=int(input("inserisci valore     "))
b:int=int(input("inserisci valore     "))
list_a:list=[a]
list_b:list=[b]


if len(list_a)>len(list_b):
    for i in range (len(list_a)-len(list_b)):
        list_b.insert(0,0)
        for i in range(len(list_a)):
            x=(list_a[-1::-1]+list_b[-1::-1])
            print(f" la somma binaria è {x} ")
    
else: 
    len(list_b)>len(list_a)
    for i in range (len(list_b)-len(list_a)):
        list_a.insert(0,0)
        for i in range(len(list_b)):
            x=(list_a[-1::-1]+list_b[-1::-1])
            print(f" la somma binaria è {x} ")
            

    