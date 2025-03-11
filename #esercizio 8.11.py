#esercizio 8.11
frasi:list=[
    "ho molto sonno",
    "ho molta fame",
    "devo studiare di +"
]



def show_message(frasi:str)->str:
    for i in frasi:
        print(i)
        return frasi




send_message:list=[]
def send_messages(send_message:str)->str:
    for i in frasi:
        send_message.append(i)
        print(*send_message)
        return send_message
send_messages(send_message)
show_message(frasi)

print(show_message(frasi))
print(send_messages(send_message))