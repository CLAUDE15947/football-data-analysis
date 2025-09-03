import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df_equipes = pd.read_csv("stats_equipes_whoscored_clean.csv")

# classement des équipes selon la possesion 
df_equipes_sorted = df_equipes.sort_values(by="Possession_pct", ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=df_equipes_sorted["Possession_pct"], y=df_equipes_sorted["Équipe"], palette="coolwarm")
plt.title("Possession moyenne des équipes (%)")
plt.xlabel("Possession (%)")
plt.ylabel("Équipe")
plt.show()

