import random
import time

from loguru import logger

from scraper import interface as scraper


def requests_if_possible(request_manager):
    if scraper.is_running():
        logger.debug("Scraper déjà en fonctionnement")
        time.sleep(2)
        return True

    if request_manager.config_dict.get('current_delta_requests_number') < request_manager.config_dict.get(
            'requests_number'):
        logger.debug("Traitement de la requete")

        request = request_manager.queue.pop(0)

        wait_time = random.randint(2, 8)
        logger.info(f"Requests Manager : met du délai aléatoire ({wait_time}) avant de faire la requete")
        time.sleep(wait_time)

        group, pages_number = request.get_group(), request.get_nb_pages()

        size_o, urls = 0, [None]

        try:

            urls = group.get_all_urls()

            size_o = scraper.start_scraping(urls, pages_number)

        except Exception as e:
            logger.error(f"Requests Manager -> Scraper: Erreur lors du scraping : {e}")

        request_manager.config_dict['total_scrap_o'] += size_o
        request_manager.config_dict['total_scrap'] = request_manager.config_dict.get('total_scrap') + len(
            urls) * pages_number
        request_manager.config_dict['current_delta_requests_number'] += len(urls) * pages_number

        return True

    logger.debug(
        f"Ne traite pas la requete car {request_manager.config_dict.get('current_delta_requests_number')}"
        f" ont déjà été faites")
    return False
