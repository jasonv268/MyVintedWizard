import time
import random
import threading

from loguru import logger
from playwright.sync_api import sync_playwright

from scraper.engine.parsing import parser
from scraper.engine.files_manager import saver


class Scraper:

    def __init__(self):
        self.working = False

    def is_running(self):
        return self.working

    def start_scraping(self, urls, nb_pages):
        total_size_o = 0
        if not self.working:
            self.working = True
            window = True
            if window:
                logger.info("WebDriver : Lancement en mode fenetré")
                with sync_playwright() as playwright:
                    browser = playwright.firefox.launch(headless=(not window))

                    for (ide, url) in urls:
                        for i in range(1, nb_pages + 1):
                            logger.debug(f"Scraper : accède à la page d'url : {url}&page={str(i)}")

                            page, size = self.get_page_source(browser, url + "&page=" + str(i))
                            total_size_o += size

                            if page is not None:
                                logger.info("Scraper : contenu de la page récupéré")
                                df = parser.parse_page_articles(page)

                                start = time.time()

                                thread = threading.Thread(target=saver.add_dataframe, args=(df, ide))
                                thread.start()
                                thread.join()

                                time.sleep(random.randint(5, 10))

                    logger.info("WebDriver : Fenetre fermée")
                    self.working = False
        return total_size_o

    @staticmethod
    def get_page_source(browser, url: str):

        def route_intercept(route):
            if route.request.resource_type == "image":
                return route.abort()
            return route.continue_()

        try:
            page = browser.new_page()
            #page.route("**/*", route_intercept)
            logger.debug("WebDriver : attend que la page soit chargée")
            page.goto(url, timeout=30000)
            page.wait_for_selector('.feed-grid')
            time.sleep(2)
            logger.debug("WebDriver : page chargée")
            content = page.content().encode('utf-8')
            content_size = len(content)
            page.close()  # Assurez-vous de fermer la page après utilisation
            return content, content_size
        except TimeoutError:
            return None


scraper = Scraper()
