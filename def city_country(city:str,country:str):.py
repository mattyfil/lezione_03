def city_country(city:str,country:str):
        city:str=" "
        country:str=" "
        city_list:list=[]
        country_list:list=[]
        city_list.append(city)
        country_list.append(country)
        
        print(f"{city} : {country}")


        

print(*city_country(roma="italy",lisbona="portogallo",toyko="giappone"))
