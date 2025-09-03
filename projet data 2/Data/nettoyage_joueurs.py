import pandas as pd 
import numpy as np 

df = pd.read_csv("Data/stats_joueurs_whoscored.csv")

print (df.head())
print( df.info())
print(df.shape)
print (df.describe())

print(df.isnull().sum()) # nombres de valeurs manquantes par colonnes 

print(df[df.isnull().any(axis=1)]) # afficher les lignes contenant les valeurs manquantes

df= df.dropna() # Supprimer les lignes avec des valeurs

df= df.dropna(axis=1) # supprimer les colonnes contenant des NaN

print(df.duplicated().sum())  # Nombre de lignes dupliquées 
print(df[df.duplicated()])  # Afficher les doublons

df = df.drop_duplicates() # Supprimer les lignes dupliquées

# Séparation des apparitions en titulaires et remplaçants
df["Apps_Titulaires"] = df["Apps"].str.extract(r'(\d+)').astype(float)
df["Apps_Remplaçants"] = df["Apps"].str.extract(r'\((\d+)\)').fillna(0).astype(float)

# Remplacement des tirets par 0 ou NaN
df["Rouges"] = df["Rouges"].replace("-", 0).astype(int)
df["Duels aériens"] = df["Duels aériens"].replace("-", np.nan).astype(float)

# Renommage des colonnes
df.rename(columns={
    "Passes%": "Passes_pct",
    "Duels aériens": "Duels_aériens"
}, inplace=True)

# Suppression de la colonne originale "Apps"
df.drop(columns=["Apps"], inplace=True)





# Sauvegarde des fichiers nettoyés
df.to_csv("stats_joueurs_whoscored_clean.csv", index=False)




