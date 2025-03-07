def check_each(number_list):
    for element in number_list:
        if element>5:
            print(f"{element} sono maggiori di 5")
        elif element<5:
            print(f"{element} sono minori di 5")
        else:
            print(f"{element} sono uguali a 5")