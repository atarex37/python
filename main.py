import logging

# Configurer un gestionnaire de fichier pour le journal du fichier principal
main_logger = logging.getLogger('main')
main_logger.setLevel(logging.DEBUG)

# Créer un gestionnaire de fichier pour enregistrer les journaux du fichier principal
main_log_handler = logging.FileHandler('main.log')
main_log_handler.setLevel(logging.DEBUG)

# Définir un format de journal personnalisé
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
main_log_handler.setFormatter(formatter)

# Ajouter le gestionnaire de fichier au logger principal
main_logger.addHandler(main_log_handler)

# Appel à une fonction ou une méthode dans le module
import module
module.some_function()
