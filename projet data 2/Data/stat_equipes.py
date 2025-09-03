import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import random
from selenium_stealth import stealth
import mysql.connector

# 🛠 Configuration du Navigateur
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

# 🎭 Ajout d'un User-Agent aléatoire pour éviter la détection
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
]
options.add_argument(f"user-agent={random.choice(user_agents)}")

# 🚀 Lancement de Chrome avec undetected-chromedriver
driver = uc.Chrome(options=options)

# 🛡️ Masquer Selenium pour éviter la détection
stealth(driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True
)

# 🔗 URL de la page des statistiques des équipes
url = "https://www.whoscored.com/Statistics"
driver.get(url)
print("✅ Page WhoScored chargée, en attente des données...")

# ⏳ Attente du chargement du tableau des équipes
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//table[@id='top-team-stats-summary-grid']"))
    )
    time.sleep(random.randint(3, 6))  # Délai aléatoire
except:
    print("❌ Erreur : Tableau des équipes non trouvé.")
    driver.quit()
    exit()

# 📊 Stockage des statistiques des équipes
stats_equipes = []
rows = driver.find_elements(By.CSS_SELECTOR, "#top-team-stats-summary-content tr")

for row in rows[:20]:  # 🔥 Prendre uniquement les 20 premières équipes
    columns = row.find_elements(By.TAG_NAME, "td")
    
    if len(columns) < 9:
        continue  # Ignore les lignes incomplètes

    # 🏆 Récupération des données avec classement
    classement = columns[0].text.strip().split(".")[0]  # Extraction du classement
    equipe = columns[0].find_element(By.CSS_SELECTOR, "a.team-link").text.strip()
    competition = columns[1].text.strip()
    buts = columns[2].text.strip()
    tirs_pm = columns[3].text.strip()
    
    # Discipline (cartons jaunes et rouges)
    try:
        cartons_jaunes = columns[4].find_element(By.CSS_SELECTOR, "span.yellow-card-box").text.strip()
    except:
        cartons_jaunes = "0"
    try:
        cartons_rouges = columns[4].find_element(By.CSS_SELECTOR, "span.red-card-box").text.strip()
    except:
        cartons_rouges = "0"

    possession = columns[5].text.strip()
    passes_reussies = columns[6].text.strip()
    aeriens_gagnes = columns[7].text.strip()
    note = columns[8].text.strip()

    # 📌 Stockage dans la liste
    equipe_data = [classement, equipe, competition, buts, tirs_pm, cartons_jaunes, cartons_rouges, possession, passes_reussies, aeriens_gagnes, note]
    stats_equipes.append(equipe_data)

# 🚪 Fermeture du navigateur
driver.quit()

# 🔄 Création d'un DataFrame
df = pd.DataFrame(stats_equipes, columns=[
    "Classement", "Équipe", "Compétition", "Buts", "Tirs/match", "Cartons jaunes", "Cartons rouges",
    "Possession%", "Passes réussies%", "Duels aériens gagnés", "Note"
])

# ✅ Vérification et correction des valeurs manquantes
df.fillna("-", inplace=True)

# 📌 **Affichage propre sans traits ni index**
print(df.to_string(index=False))

# 💾 Sauvegarde en CSV
df.to_csv("stats_equipes_whoscored.csv", index=False, encoding="utf-8")
print("\n✅ Statistiques enregistrées dans 'stats_equipes_whoscored.csv'")

# 🛠 Connexion à MySQL
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="footballstats"
    )
    cursor = db.cursor()

    # 📌 Création de la table MySQL si elle n'existe pas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stats_equipes (
            classement INT PRIMARY KEY,
            equipe VARCHAR(255),
            competition VARCHAR(255),
            buts INT,
            tirs_match FLOAT,
            cartons_jaunes INT,
            cartons_rouges INT,
            possession FLOAT,
            passes_reussies FLOAT,
            duels_aeriens_gagnes FLOAT,
            note FLOAT
        )
    """)

    # 🚀 Insertion des données avec mise à jour en cas de doublon
    for equipe in stats_equipes:
        cursor.execute("""
            INSERT INTO stats_equipes (classement, equipe, competition, buts, tirs_match, cartons_jaunes, cartons_rouges, possession, passes_reussies, duels_aeriens_gagnes, note)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            buts=VALUES(buts), tirs_match=VALUES(tirs_match), cartons_jaunes=VALUES(cartons_jaunes), cartons_rouges=VALUES(cartons_rouges),
            possession=VALUES(possession), passes_reussies=VALUES(passes_reussies), duels_aeriens_gagnes=VALUES(duels_aeriens_gagnes), note=VALUES(note)
        """, equipe)

    db.commit()
    print("\n✅ Données insérées dans la base de données MySQL.")

except mysql.connector.Error as e:
    print(f"❌ Erreur MySQL : {e}")

finally:
    cursor.close()
    db.close()
    print("🔌 Connexion MySQL fermée.")
