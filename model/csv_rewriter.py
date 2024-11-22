import pandas as pd

class CsvRewriter:
    def __init__(self, file_name=None):
        """
        Initialise avec le nom du fichier à manipuler.
        """
        self.file_name = file_name
        self.df = None

    def load_csv(self):
        """
        Charge le fichier CSV dans un DataFrame pandas.
        """
        if not self.file_name:
            raise ValueError("Le nom du fichier n'a pas été défini.")
        self.df = pd.read_csv(self.file_name)
        print(f"Fichier chargé : {self.file_name}")

    def save_csv(self, output_name=None):
        """
        Sauvegarde le DataFrame dans un fichier CSV. Si aucun nom n'est spécifié, un nom par défaut est utilisé.
        """
        if self.df is None:
            raise ValueError("Aucun fichier n'a été chargé.")
        if not output_name:
            output_name = "./recording_output.csv"
        self.df.to_csv(output_name, index=False)
        print(f"Fichier sauvegardé sous : {output_name}")

    def remove_columns(self, columns_to_remove):
        """
        Supprime les colonnes spécifiées du DataFrame.
        """
        if self.df is None:
            raise ValueError("Aucun fichier n'a été chargé.")
        if self.df.columns.size > 0:  # Vérifie qu'il y a des colonnes
            columns_to_remove.append(self.df.columns[0])
        self.df = self.df.drop(columns=columns_to_remove, errors="ignore")
        print(f"Colonnes supprimées : {columns_to_remove}")
