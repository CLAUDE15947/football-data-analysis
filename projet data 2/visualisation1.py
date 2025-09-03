

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données nettoyées
df_joueurs = pd.read_csv("stats_joueurs_whoscored_clean.csv")

# 📊 Histogramme des buts
sns.histplot(df_joueurs["Buts"], bins=10, kde=True)
plt.title("Distribution des buts marqués")
plt.xlabel("Nombre de buts")
plt.ylabel("Nombre de joueurs")
plt.show()

# 📊 Nuage de points : Passes réussies vs Buts
sns.scatterplot(x=df_joueurs["Passes_pct"], y=df_joueurs["Buts"])
plt.title("Relation entre passes réussies et buts marqués")
plt.xlabel("Passes réussies (%)")
plt.ylabel("Nombre de buts")
plt.show()

# Meilleur butteur du championnat 

df_top_buteurs = df_joueurs.sort_values(by="Buts", ascending=False).head(10)  # Top 10 buteurs

plt.figure(figsize=(10, 6))
sns.barplot(x=df_top_buteurs["Buts"], y=df_top_buteurs["Joueur"], palette="Reds_r")
plt.title("Top 10 des meilleurs buteurs")
plt.xlabel("Buts marqués")
plt.ylabel("Joueur")
plt.show()