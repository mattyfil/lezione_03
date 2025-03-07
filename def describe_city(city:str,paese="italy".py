def describe_city(city:str,paese="italy"):
    return city,paese


print(*describe_city("londra","inghilterra"))
print(*describe_city("roma,italy"))
print(*describe_city("tokyo","giappone"))
