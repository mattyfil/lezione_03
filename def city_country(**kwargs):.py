def city_country(**kwargs):
   for k,v in  kwargs.items():
      print(f"{k},{v}")
      
print(city_country(roma="italy",toyko="giappone",lisbona="portogallo"))
