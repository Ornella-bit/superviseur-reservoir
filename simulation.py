import time
import random

# --- Paramètres ---
SEUIL_BAS = 30.0          # la pompe démarre en dessous
SEUIL_HAUT = 80.0         # la pompe s'arrête au-dessus
CONSOMMATION = 2.0        # perte de niveau par pas
DEBIT_POMPE = 5.0         # gain de niveau par pas (pompe ON)

ALARME_NIVEAU_BAS = 15.0
ALARME_NIVEAU_HAUT = 95.0
ALARME_TEMPERATURE = 40.0

# --- État initial ---
niveau = 50.0
temperature = 25.0
pompe_active = False

for pas in range(1, 101):
    niveau_precedent = niveau

    # 1. Décision : la pompe doit-elle tourner ?
    if niveau < SEUIL_BAS:
        pompe_active = True
    elif niveau > SEUIL_HAUT:
        pompe_active = False

    # 2. Le niveau évolue (limité entre 0 et 100 %)
    niveau = niveau - CONSOMMATION
    if pompe_active:
        niveau = niveau + DEBIT_POMPE
    niveau = max(0.0, min(100.0, niveau))

    # 3. La température évolue (la pompe chauffe, sinon refroidissement)
    if pompe_active:
        temperature = temperature + 1.2
    else:
        temperature = temperature - 0.5
    temperature = temperature + random.uniform(-0.2, 0.2)  # bruit du capteur
    temperature = max(25.0, temperature)                   # pas sous 25 °C

    # 4. Alarmes
    alarmes = []
    if niveau < ALARME_NIVEAU_BAS:
        alarmes.append("NIVEAU BAS")
    if niveau > ALARME_NIVEAU_HAUT:
        alarmes.append("NIVEAU HAUT")
    if temperature > ALARME_TEMPERATURE:
        alarmes.append("TEMPERATURE HAUTE")
    if pompe_active and niveau < niveau_precedent:
        alarmes.append("POMPE INEFFICACE")

    # 5. Affichage
    etat = "ON" if pompe_active else "OFF"
    texte_alarmes = ", ".join(alarmes) if alarmes else "-"
    print(f"Pas {pas:3d} | Niveau : {niveau:5.1f} % | Temp : {temperature:4.1f} °C | Pompe : {etat:3} | Alarmes : {texte_alarmes}")
    time.sleep(0.2)
    