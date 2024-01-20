import logging

# Configurer un gestionnaire de fichier pour le journal du module
module_logger = logging.getLogger('module')
module_logger.setLevel(logging.DEBUG)

# Créer un gestionnaire de fichier pour enregistrer les journaux du module
module_log_handler = logging.FileHandler('module.log')
module_log_handler.setLevel(logging.DEBUG)

# Définir un format de journal personnalisé
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
module_log_handler.setFormatter(formatter)

# Ajouter le gestionnaire de fichier au logger du module
module_logger.addHandler(module_log_handler)

def some_function():
    # Utilisez le logger du module pour enregistrer des messages
    module_logger.debug("Ceci est un message de débogage du module.")
    module_logger.info("Ceci est un message d'information du module.")
    module_logger.warning("Ceci est un message d'avertissement du module.")
