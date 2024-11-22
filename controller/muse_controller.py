from model.csv_rewriter import CsvRewriter
from model.eeg_recorder import EegRecorder

class MuseController:
    def __init__(self):
        """
        Initialise le contrôleur avec une instance d'EegRecorder et de CsvRewriter.
        """
        self.eeg_recorder = EegRecorder()
        self.csv_rewriter = CsvRewriter()

    def run(self):
        """
        Exécute les étapes du programme :
        1. Collecte des données EEG
        2. Chargement des données CSV
        3. Modification des données
        3. Sauvegarde des modifications

        """
        try:
            # Étape 1 : Collecter les données EEG
            csv_file = self.eeg_recorder.record_eeg(duration=60)

            # Étape 2 : Charger les données dans le modèle CSV
            self.csv_rewriter.file_name = csv_file
            self.csv_rewriter.load_csv()

            # Étape 3 : Supprimer des colonnes inutiles
            columns_to_remove = ["Right AUX", "timestamps"]
            self.csv_rewriter.remove_columns(columns_to_remove)

            # Étape 4 : Sauvegarder le fichier modifié
            output_name = input("Entrez le nom du fichier de sortie (laisser vide pour le nom par défaut) : ")
            self.csv_rewriter.save_csv(output_name if output_name else None)

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
