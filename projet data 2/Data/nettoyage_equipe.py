import pandas as pd
import numpy as np

df_equipes = pd.read_csv("Data/stats_equipes_whoscored.csv")

# Nettoyage du fichier des équipes
# Suppression du numéro devant les noms des équipes
df_equipes["Équipe"] = df_equipes["Équipe"].str.replace(r'^\d+\.\s', '', regex=True)

# Renommage des colonnes
df_equipes.rename(columns={
    "Possession%": "Possession_pct",
    "Passes réussies%": "Passes_reussies_pct"
}, inplace=True)

df_equipes.to_csv("stats_equipes_whoscored_clean.csv", index=False)