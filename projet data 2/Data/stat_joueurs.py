import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# 🛠 Configuration de Selenium
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")

# 🔥 Lancement du navigateur
driver = webdriver.Chrome(service=service, options=options)

# 📌 URL de la page WhoScored
url = "https://www.whoscored.com/Statistics"
driver.get(url)
print("✅ Page WhoScored chargée, en attente des données...")

# Attente du tableau des joueurs
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//table[@id='top-player-stats-summary-grid']"))
)
time.sleep(5)

# 📊 Stockage des statistiques des joueurs
stats_joueurs = []
players_count = 0  

while players_count < 10:
    print(f"📄 Scraping des joueurs... Total actuel : {players_count}")

    rows = driver.find_elements(By.CSS_SELECTOR, "#player-table-statistics-body tr")

    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")

        if len(columns) < 13:
            print(f"❌ Ligne ignorée (nombre de colonnes insuffisant) : {len(columns)} colonnes trouvées")
            continue  

        # **Récupération propre du nom du joueur (sans numéro)**
        try:
            joueur_nom = columns[0].find_element(By.CSS_SELECTOR, "span.iconize").text.strip()
        except:
            joueur_nom = columns[0].find_element(By.TAG_NAME, "a").text.strip()  # Plan B

        # **Récupérer les autres infos via les bons `<span>`**
        try:
            equipe = columns[0].find_element(By.CSS_SELECTOR, "span.team-name").text.strip()
        except:
            equipe = "-"

        try:
            age = columns[0].find_element(By.CSS_SELECTOR, "span.player-meta-data:nth-of-type(1)").text.strip()
        except:
            age = "0"

        try:
            poste = columns[0].find_element(By.CSS_SELECTOR, "span.player-meta-data:nth-of-type(2)").text.strip()
        except:
            poste = "-"

        # **Convertir `age` en INT et gérer les erreurs**
        try:
            age = int(age)
        except ValueError:
            age = 0  # Si l'âge est invalide, mettre 0

        # 📌 **Décaler les valeurs de -1 pour corriger le décalage**
        valeurs = [col.text.strip() for col in columns[1:]]
        valeurs = valeurs[1:]  # Décale les valeurs d'une colonne vers la gauche

        # 🚀 **Suppression des colonnes en trop**
        valeurs = valeurs[:11]  # On garde exactement 11 valeurs après correction

        # **Ajout du numéro de classement (ID = Classement)**
        joueur_data = [players_count + 1, joueur_nom, equipe, age, poste] + valeurs

        print(joueur_data)  # 🔍 Vérification
        stats_joueurs.append(joueur_data)
        players_count += 1  

        if players_count >= 10:
            break  

    try:
        next_button = driver.find_element(By.XPATH, "//a[@id='next' and contains(@class, 'clickable')]")
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(5)  
    except:
        print("❌ Fin de la pagination ou erreur de chargement.")
        break  

driver.quit()

# 🔄 Création d'un DataFrame avec numéro de classement en première colonne
df = pd.DataFrame(stats_joueurs, columns=[
    "ID", "Joueur", "Équipe", "Âge", "Poste", "Apps", "Minutes", "Buts", "Passes", "Jaunes", "Rouges",
    "Tirs/match", "Passes%", "Duels aériens", "Homme du match", "Note"
])

# ✅ Vérification et correction des valeurs manquantes
df.fillna("-", inplace=True)

# 📌 **Affichage propre avec le numéro de classement bien aligné**
print(df.to_string(index=False))

# 💾 Sauvegarde en CSV
df.to_csv("stats_joueurs_whoscored.csv", index=False, encoding="utf-8")
print("\n✅ Statistiques enregistrées dans 'stats_joueurs_whoscored.csv'")

# 🛠 Connexion à MySQL
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",      
        password="",      
        database="footballstats"
    )
    cursor = db.cursor()

    # 📌 **Correction de la structure MySQL : ID = Classement**
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stats_joueurs (
            id INT PRIMARY KEY,
            joueur VARCHAR(255),
            equipe VARCHAR(255),
            age INT,  
            poste VARCHAR(50),
            apps VARCHAR(10),
            minutes INT,
            buts INT,
            passes INT,
            jaunes INT,
            rouges INT,
            tirs_match FLOAT,
            passes_pourcent FLOAT,
            duels_aeriens FLOAT,
            homme_du_match INT,
            note FLOAT
        )
    """)

    # 🚀 Insertion des données avec `ID = Classement`
    for joueur in stats_joueurs:
        cursor.execute("""
            INSERT INTO stats_joueurs (id, joueur, equipe, age, poste, apps, minutes, buts, passes, jaunes, rouges, tirs_match, passes_pourcent, duels_aeriens, homme_du_match, note)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, joueur)  # L'ID est maintenant la première valeur dans `joueur`

    db.commit()  
    print("\n✅ Données insérées dans la base de données MySQL.")

except mysql.connector.Error as e:
    print(f"❌ Erreur MySQL : {e}")

finally:
    cursor.close()
    db.close()
    print("🔌 Connexion MySQL fermée.")
