from scraper.engine.scraping.scraper import scraper

from scraper.engine.scraping.scraper import scraper


def start_scraping(requests, nb_page):
    """
    Démarre le processus de scraping avec les requêtes et le nombre de pages spécifiés.

    Args:
        requests (list): Liste des requêtes à scraper.
        nb_page (int): Nombre de pages à scraper par requête.

    Raises:
        ValueError: Si nb_page est inférieur ou égal à zéro.
        Exception: En cas d'échec du scraping.

    Returns:
        None
    """
    if nb_page <= 0:
        raise ValueError("Le nombre de pages doit être supérieur à zéro.")

    try:
        return scraper.start_scraping(requests, nb_page)
    except Exception as e:
        raise Exception(f"Une erreur s'est produite lors du scraping : {str(e)}")


def is_running():
    """
    Vérifie si le processus de scraping est en cours d'exécution.

    Returns:
        bool: True si le processus est en cours d'exécution, False sinon.
    """
    return scraper.is_running()
