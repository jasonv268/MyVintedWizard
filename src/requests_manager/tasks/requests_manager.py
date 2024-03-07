import json
import threading
import time
from pathlib import Path

from loguru import logger

from requests_manager.tasks import helper

config_path = Path("requests_manager/tasks/config.json")


class RequestsManager:

    def __init__(self):
        self.queue = []

        self.requests_thread = None

        with open(config_path) as config_file:
            self.config_dict = json.load(config_file)

        logger.debug(f"Requests Manager : instancié avec ces params : {self.config_dict}")

        self.notify_event = threading.Event()
        self.running = False

    def init(self, requests_number=None, delta_time=None):
        if requests_number and delta_time:
            self.config_dict['requests_number'] = requests_number
            self.config_dict['delta_duration'] = delta_time

        self.save_config()

        logger.info(f"Requests Manager : initialisé avec ces params : {self.config_dict}")

    def reinit(self, requests_number=None, delta_time=None):
        self.config_dict['init_time'] = time.time()
        self.config_dict['total_scrap'] = 0
        self.config_dict['total_scrap_o'] = 0
        self.config_dict['current_delta_init_time'] = time.time()
        self.config_dict['current_delta_requests_number'] = 0
        if requests_number and delta_time:
            self.config_dict['requests_number'] = requests_number
            self.config_dict['delta_duration'] = delta_time

        self.save_config()

        logger.info(f"Requests Manager : réinitialisé avec ces params : {self.config_dict}")

    def save_config(self):
        with open(config_path, 'w') as config_file:
            json.dump(self.config_dict, config_file, indent=4)
        logger.debug(f"Requests Manager : configuration sauvegardée avec ces params : {self.config_dict}")

    def run(self):

        while self.running:

            logger.debug("Requests Manager : en attente pour économiser les ressources")
            self.notify_event.wait()  # Attendre jusqu'à ce qu'un nouveau message soit disponible
            logger.debug("Requests Manager : en action")

            self.config_dict['current_delta_init_time'] = time.time()
            self.config_dict['current_delta_requests_number'] = 0
            logger.debug("Requests Manager : nouvelle fenetre d'autorisation")

            while len(self.queue) > 0:

                if helper.requests_if_possible(self):
                    logger.debug(f"Requests Manager : requete effectuée")

                else:
                    wait_time = self.config_dict['delta_duration'] - (
                            time.time() - self.config_dict['current_delta_init_time'])
                    logger.debug(f"Requests Manager : attend {wait_time} s pour la prochaine fenetre d'autorisation ")
                    time.sleep(wait_time)
                    self.config_dict['current_delta_init_time'] = time.time()
                    self.config_dict['current_delta_requests_number'] = 0
                    logger.debug("Requests Manager : nouvelle fenetre d'autorisation")

            self.notify_event.clear()

    def launch(self):
        if self.running is False:
            logger.info("Requests Manager : lance le limiteur")
            self.running = True
            self.requests_thread = threading.Thread(target=self.run)
            self.requests_thread.start()
            logger.debug("Requests Manager : thread lancé")

    def stop(self):
        if self.running:
            logger.info("Requests Manager : stoppe le limiteur")
            self.running = False
            #self.requests_thread.join()
            logger.debug(f"Requests Manager : thread terminé")
            self.save_config()

    def ask_for_request(self, request):
        logger.info("Requests Manager : requete reçue")
        self.queue.append(request)
        self.notify_event.set()
        logger.debug("Requests Manager : notification envoyée au thread")


requestsmg = RequestsManager()
