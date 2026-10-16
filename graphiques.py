import pandas as pd
import matplotlib.pyplot as plt

# --- Lecture du CSV ---
df = pd.read_csv("donnees.csv")

# Les lignes où la colonne "alarmes" n'est pas vide
en_alarme = df[df["alarmes"].notna()]

# --- Trois graphiques empilés, avec le même axe horizontal ---
fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

# 1. Niveau
axes[0].plot(df["pas"], df["niveau"], color="tab:blue", label="Niveau")
axes[0].axhline(30, color="gray", linestyle="--", label="Seuil bas pompe (30 %)")
axes[0].axhline(80, color="gray", linestyle=":", label="Seuil haut pompe (80 %)")
axes[0].scatter(en_alarme["pas"], en_alarme["niveau"], color="red", s=20, label="Alarme active")
axes[0].set_ylabel("Niveau (%)")
axes[0].set_title("Superviseur de réservoir simulé")
axes[0].legend(loc="upper right", fontsize=8)

# 2. Température
axes[1].plot(df["pas"], df["temperature"], color="tab:orange", label="Température")
axes[1].axhline(40, color="red", linestyle="--", label="Alarme (40 °C)")
axes[1].set_ylabel("Température (°C)")
axes[1].legend(loc="upper right", fontsize=8)

# 3. Pompe
axes[2].step(df["pas"], df["pompe"], where="post", color="tab:green")
axes[2].set_yticks([0, 1])
axes[2].set_yticklabels(["OFF", "ON"])
axes[2].set_ylabel("Pompe")
axes[2].set_xlabel("Pas de simulation")

plt.tight_layout()
plt.savefig("graphiques.png", dpi=150)
plt.show()
