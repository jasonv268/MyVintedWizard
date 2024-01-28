import threading
import time
import random

from selenium import webdriver

from stats_manager.utils.parsing import parser

from stats_manager.utils.files_manager import saver

from selenium.webdriver.firefox.options import Options

gecko_driver_path = '/user/local/bin/geckodriver'


def start_web_driver_window():
    firefox_options = Options()
    firefox_options.add_argument('--headless')
    driver = webdriver.Firefox(options=firefox_options)

    return driver


def start_scraping(requests, nb_page):

    #thread = threading.Thread(target=collect_data, args=(requests, nb_page))
    #thread.start()
    collect_data(requests, nb_page)


def collect_data(urls, nb_pages):
    driver = start_web_driver_window()
    for (ide, url) in urls:
        for i in range(1, 2):
            page = get_page_source(driver, url + "&page=" + str(i))

            # parser la page
            df = parser.parse_page_articles(page)

            # enregistrer toutes les données
            saver.save_dataframe(df, ide)
            time.sleep(random.randint(5, 10))


def get_page_source(web_driver, url: str):
    web_driver.get(url)
    time.sleep(2)
    return web_driver.page_source.encode('utf-8')
