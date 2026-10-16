import csv
import random
import time
from dataclasses import dataclass

# --- Paramètres ---
SEUIL_BAS = 30.0
SEUIL_HAUT = 80.0
CONSOMMATION = 2.0
DEBIT_POMPE = 5.0

ALARME_NIVEAU_BAS = 15.0
ALARME_NIVEAU_HAUT = 95.0
ALARME_TEMPERATURE = 40.0

def clamp(valeur, minimum, maximum):
    return max(minimum, min(maximum, valeur))

@dataclass
class Reservoir:
    niveau: float = 50.0
    temperature: float = 25.0
    pompe_active: bool = False

    def decide_pompe(self):
        if self.niveau < SEUIL_BAS:
            self.pompe_active = True
        elif self.niveau > SEUIL_HAUT:
            self.pompe_active = False

    def update_state(self):
        niveau_precedent = self.niveau

        self.decide_pompe()

        # Niveau
        self.niveau -= CONSOMMATION
        if self.pompe_active:
            self.niveau += DEBIT_POMPE
        self.niveau = clamp(self.niveau, 0.0, 100.0)

        # Température
        if self.pompe_active:
            self.temperature += 1.2
        else:
            self.temperature -= 0.5

        self.temperature += random.uniform(-0.2, 0.2)
        self.temperature = max(25.0, self.temperature)

        alarmes = self.detect_alarmes(niveau_precedent)
        return alarmes

    def detect_alarmes(self, niveau_precedent):
        alarmes = []

        if self.niveau < ALARME_NIVEAU_BAS:
            alarmes.append("NIVEAU BAS")
        if self.niveau > ALARME_NIVEAU_HAUT:
            alarmes.append("NIVEAU HAUT")
        if self.temperature > ALARME_TEMPERATURE:
            alarmes.append("TEMPERATURE HAUTE")
        if self.pompe_active and self.niveau < niveau_precedent:
            alarmes.append("POMPE INEFFICACE")

        return alarmes

    def afficher(self, pas, alarmes):
        etat = "ON" if self.pompe_active else "OFF"
        texte_alarmes = ", ".join(alarmes) if alarmes else "-"
        print(
            f"Pas {pas:3d} | Niveau : {self.niveau:5.1f} % | "
            f"Temp : {self.temperature:4.1f} °C | Pompe : {etat:3} | "
            f"Alarmes : {texte_alarmes}"
        )

def simuler():
    random.seed(42)  # pour reproduire le même comportement
    reservoir = Reservoir()

    for pas in range(1, 101):
        alarmes = reservoir.update_state()
        reservoir.afficher(pas, alarmes)
        time.sleep(0.2)

if __name__ == "__main__":
    def simuler():
        random.seed(42)  # pour reproduire le même comportement
    reservoir = Reservoir()

    with open("donnees.csv", "w", newline="", encoding="utf-8") as fichier:
        ecrivain = csv.writer(fichier)
        ecrivain.writerow(["pas", "niveau", "temperature", "pompe", "alarmes"])

        for pas in range(1, 101):
            alarmes = reservoir.update_state()
            reservoir.afficher(pas, alarmes)
            ecrivain.writerow([
                pas,
                round(reservoir.niveau, 1),
                round(reservoir.temperature, 1),
                1 if reservoir.pompe_active else 0,
                "|".join(alarmes),
            ])
            time.sleep(0.2)

