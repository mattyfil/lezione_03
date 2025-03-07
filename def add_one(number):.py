def add_one(number):
   return number+1


def add_one_to_list(numero_lista):
   nuova_lista=[]
   for number in numero_lista:
      nuova_lista.append(add_one(number))
      print(nuova_lista)
