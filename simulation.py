import time

niveau = 0.0               # le réservoir démarre vide
debit_remplissage = 5.0    # +5 % par pas
consommation = 2.5         # -2,5 % par pas

print("--- Remplissage ---")
while niveau < 100:
    niveau = niveau + debit_remplissage
    print(f"Niveau du réservoir : {niveau:.1f} %")
    time.sleep(0.3)

print("--- Consommation ---")
while niveau > 0:
    niveau = niveau - consommation
    print(f"Niveau du réservoir : {niveau:.1f} %")
    time.sleep(0.3)

print("Cycle terminé")
