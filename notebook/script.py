import pandas as pd
import logging

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Début du script")

    # 1. Chargement des données
    df = pd.read_csv("data.csv", encoding="utf-8-sig")
    logging.info("Données chargées")

    # 2. Nettoyage des colonnes
    df.columns = df.columns.str.strip()
    logging.info("Colonnes nettoyées")

    # 3. Agrégation (évolution)
    evolution = (
        df.groupby(["Année", "Cotisations/prestations"])["Montant"]
        .sum()
        .reset_index()
    )
    logging.info("Table evolution calculée")

    # 4. Sauvegarde (important ✅)
    evolution.to_csv("evolution.csv", index=False)
    logging.info("Fichier evolution.csv sauvegardé")

    logging.info("Fin du script")

if __name__ == "__main__":
    main()


