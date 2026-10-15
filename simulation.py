import time

niveau = 50.0          # niveau du réservoir en %
consommation = 2.5     # le niveau baisse de 2,5 % par seconde

while niveau > 0:
    print(f"Niveau du réservoir : {niveau:.1f} %")
    niveau = niveau - consommation
    time.sleep(1)      # attend 1 seconde

print("Réservoir vide !")

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

import time

SEUIL_BAS = 30.0      # la pompe démarre en dessous
SEUIL_HAUT = 80.0     # la pompe s'arrête au-dessus
CONSOMMATION = 2.0    # perte de niveau par pas (utilisation de l'eau)
DEBIT_POMPE = 5.0     # gain de niveau par pas quand la pompe tourne

niveau = 50.0
pompe_active = False

for pas in range(1, 61):
    # 1. Décision : la pompe doit-elle tourner ?
    if niveau < SEUIL_BAS:
        pompe_active = True
    elif niveau > SEUIL_HAUT:
        pompe_active = False

    # 2. Le niveau évolue
    niveau = niveau - CONSOMMATION
    if pompe_active:
        niveau = niveau + DEBIT_POMPE

    # 3. Affichage
    etat = "ON" if pompe_active else "OFF"
    print(f"Pas {pas:2d} | Niveau : {niveau:5.1f} % | Pompe : {etat}")
    time.sleep(0.2)