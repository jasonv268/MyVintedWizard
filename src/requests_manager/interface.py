from requests_manager.tasks.requests_manager import requestsmg
from requests_manager.tasks.Request import Request


def launch():
    """
    Lance le gestionnaire de requêtes.
    """
    try:
        requestsmg.launch()
    except Exception as e:
        # Gérer l'exception
        raise Exception("Une erreur s'est produite lors du lancement du gestionnaire de requêtes : {}".format(str(e)))


def stop():
    """
    Arrête le gestionnaire de requêtes.
    """
    try:
        requestsmg.stop()
    except Exception as e:
        # Gérer l'exception
        raise Exception("Une erreur s'est produite lors de l'arrêt du gestionnaire de requêtes : {}".format(str(e)))


def init(requests_number, delta_time):
    if requests_number <= 0:
        raise ValueError("Le nombre de requêtes doit être supérieur à zéro.")
    if delta_time < 0:
        raise ValueError("Le delta de temps doit être supérieur ou égal à zéro.")

    try:
        requestsmg.init(requests_number, delta_time)
    except Exception as e:
        # Gérer l'exception
        raise Exception(
            "Une erreur s'est produite lors de l'initialisation du gestionnaire de requêtes : {}".format(str(e)))


def reinit(requests_number, delta_time):
    """
    Réinitialise le gestionnaire de requêtes avec le nombre de requêtes et le delta de temps spécifiés.

    Args:
        requests_number (int): Le nombre de requêtes à réinitialiser.
        delta_time (float): L'intervalle de temps (en secondes) entre les requêtes.

    Raises:
        ValueError: Si requests_number est inférieur ou égal à zéro ou si delta_time est négatif.
        Exception: En cas d'échec de la réinitialisation du gestionnaire de requêtes.

    Returns:
        None
    """
    if requests_number <= 0:
        raise ValueError("Le nombre de requêtes doit être supérieur à zéro.")
    if delta_time < 0:
        raise ValueError("Le delta de temps doit être supérieur ou égal à zéro.")

    try:
        requestsmg.reinit(requests_number, delta_time)
    except Exception as e:
        # Gérer l'exception
        raise Exception(
            "Une erreur s'est produite lors de la réinitialisation du gestionnaire de requêtes : {}".format(str(e)))


def ask_for_request(request):
    """
    Envoie une demande de requête au gestionnaire de requêtes.

    Args:
        request (str, str): La demande de requête à envoyer.
    """
    try:
        requestsmg.ask_for_request(request)
    except Exception as e:
        # Gérer l'exception
        raise Exception("Une erreur s'est produite lors de l'envoi de la demande de requête : {}".format(str(e)))


def create_request(group, nb_pages):
    """
       Crée une requete instance de la classe Requete.

       Args:
           group (django.db.group) : Le groupe de la base de donnée contenant les filtres sur lequel on va scraper
           nb_pages (int) : Le nombre de page que l'on va scraper par filtre
       """
    if group is None:
        raise ValueError("Le groupe n'est pas défini ou n'existe pas dans la base de donnée")
    if nb_pages < 0:
        raise ValueError("Le nombre de pages ne peut pas etre négatif")
    try:
        return Request(group, nb_pages)
    except Exception as e:
        # Gérer l'exception
        raise Exception("Une erreur s'est produite lors de l'envoi de la demande de requête : {}".format(str(e)))
