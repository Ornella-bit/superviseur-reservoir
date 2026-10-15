import time

niveau = 50.0          # niveau du réservoir en %
consommation = 2.5     # le niveau baisse de 2,5 % par seconde

while niveau > 0:
    print(f"Niveau du réservoir : {niveau:.1f} %")
    niveau = niveau - consommation
    time.sleep(1)      # attend 1 seconde

print("Réservoir vide !")