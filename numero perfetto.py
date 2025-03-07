n:int=int(input("inserisci numero naturale"))
x:list=[]
sum=0
for i in range(1,n//2+1):
    if n%i==0:
        x.append(i)
        sum+=i
'''
match n:
    case n if n==sum:
        print(f"il numero inserito è un numero perfetto")
    case _:
        print(f"non è un numero perfetto")
'''

if n==sum:
    print(f"il numero inserito è un numero perfetto")
else:
    print(f"non è un numero perfetto")



