import random
 
lietas = ("akmens", "šķēres", "papīrs")
speletajs = None 
dators = random.choice(lietas)





while speletajs not in lietas:
    speletajs = input("Ieraksti savu izvēli ( akmens, šķēres, papīrs): ")


print (f"spēlētājs: {speletajs}")
print (f"dators: {dators}")


if speletajs == dators:
    print ("Neizšķirts")
elif speletajs == "šķēŗes" and dators == "papīrs":
    print("TU UZVARĒJI!")
elif speletajs == "papīrs" and dators == "akmens":
    print("TU UZVARĒJI!")
elif speletajs == "akmens" and dators == "šķēres":
    print("TU UZVARĒJI!")
else:
    print("TU ZAUDĒJI")

    
