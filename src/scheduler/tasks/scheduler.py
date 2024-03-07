import schedule
import threading
import time

from loguru import logger

from scheduler.models import Scheduler

from requests_manager import interface as requests_manager


class SchedulerManager:

    def __init__(self):
        self.stop_event = threading.Event()
        self.stop_event.set()
        self.schedule_thread = threading.Thread(target=self.run_schedule)
        logger.debug("Scheduler: Instancié")

    def is_running(self):
        return not self.stop_event.is_set()

    @staticmethod
    def do(groups):
        for group in groups:
            logger.info(f"Scheduler : ordonne une requete pour le groupe {group}")
            requests_manager.ask_for_request((group, 1))

    def run_schedule(self):
        while not self.stop_event.is_set():
            logger.debug(f"Scheduler : en vie {self.schedule_thread.is_alive()}")
            schedule.run_pending()
            time.sleep(10)

    def launch_scheduled(self):
        if self.stop_event.is_set():
            logger.info("Scheduler : lance les taches prévues")
            schedulers = Scheduler.objects.all()
            for scheduler in schedulers:
                if scheduler.all_time_running:
                    schedule.every(scheduler.refresh_time_min).minutes.do(
                        lambda: self.do(scheduler.targeted_groups.all())
                    ).tag(scheduler.id)
                    logger.info(f"Scheduler lancé pour: {scheduler.targeted_groups.all()} "
                                f"toutes les {scheduler.refresh_time_min} min")

            self.stop_event.clear()
            if not self.schedule_thread.is_alive():
                self.schedule_thread = threading.Thread(target=self.run_schedule)
                self.schedule_thread.start()
                logger.debug(f"Scheduler : thread lancé")
            else:
                logger.debug(f"Scheduler : thread relancé")

    def stop_scheduled(self):
        if not self.stop_event.is_set():
            self.stop_event.set()
            schedule.clear()
            logger.info("Scheduler : stoppe les taches prévues")


schedulermg = SchedulerManager()
