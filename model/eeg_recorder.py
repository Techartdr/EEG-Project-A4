import os
import subprocess
import time
import shutil

class EegRecorder:
    def __init__(self, output_dir="res"):
        """
        Initialise l'enregistreur EEG avec un répertoire de sortie.
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def record_eeg(self, duration=60):
        """
        Enregistre des données EEG à l'aide d'une commande bash et retourne le chemin du fichier généré.
        """
        try:
            print("Démarrage de l'enregistrement EEG...")

            # Liste des fichiers existants dans le répertoire de travail avant l'enregistrement
            files_before = set(os.listdir("."))

            # Exécute 'muselsl stream' en arrière-plan
            stream_process = subprocess.Popen("muselsl stream", shell=True)

            # Attendre que le streaming démarre
            time.sleep(15)

            # Commande pour enregistrer les données
            bash_command = f"muselsl record --duration {duration}"
            subprocess.run(bash_command, shell=True, check=True)

            # Arrêter le streaming
            stream_process.terminate()

            # Liste des fichiers après l'enregistrement
            files_after = set(os.listdir("."))

            # Identifier le fichier créé dans le répertoire courant
            new_files = files_after - files_before
            if not new_files:
                raise RuntimeError("Aucun fichier EEG n'a été généré.")

            # Trouver le fichier CSV généré
            generated_file = next(iter(new_files))
            generated_file_path = os.path.abspath(generated_file)

            # Déplacer le fichier dans le dossier de sortie
            output_file_path = os.path.join(self.output_dir, generated_file)
            shutil.move(generated_file_path, output_file_path)

            print(f"Données EEG enregistrées dans : {output_file_path}")
            return output_file_path

        except FileNotFoundError:
            raise RuntimeError("La commande 'muselsl' n'a pas été trouvée. Assurez-vous qu'elle est installée.")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Erreur lors de la collecte des données EEG : {e}")
