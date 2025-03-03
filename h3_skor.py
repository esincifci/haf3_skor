import random

gs_gol=random.randint(0,5)
fb_gol=random.randint(0,5)

if gs_gol > fb_gol:
     print("kazanan takım:gs",gs_gol)
elif fb_gol >gs_gol:
    print("kazanan takım:fb",fb_gol)
else:
print("sonuc berabere")