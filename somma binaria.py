a:int=int(input("inserisci valore     "))
b:int=int(input("inserisci valore     "))
list_a:list=[a]
list_b:list=[b]

while len(list_a)>len(list_b):
    list_b.insert(0,0)
for i in list_a:
        x=(list_a[-1::-1]+list_b[-1::-1])
while len(list_b)>len(list_a):
    list_b.insert(0,0)
for i in list_b:
        x=(list_a[-1::-1]+list_b[-1::-1])
        print(f" la somma binaria è {x} ")





    
    
