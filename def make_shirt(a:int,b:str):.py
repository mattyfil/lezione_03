def make_shirt(a="media",z="large",y=" I love python"):
    if a!="media"or z!="large":
        print("non so che taglia è")
    return a,z,y

print(f"la maglietta scelta ha queste caratteristiche\n",*make_shirt("piccola","ho sonno"))