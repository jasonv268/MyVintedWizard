import schedule
import threading
import time

from loguru import logger

from scheduler.models import Scheduler

from requests_manager import interface as requests_manager

wait_time = 60


class SchedulerManager:

    def __init__(self):
        self.stop_event = threading.Event()
        self.stop_event.set()
        self.schedule_thread = threading.Thread(target=self.run_schedule)
        logger.debug("Scheduler: Instancié")

    def is_running(self):
        return not self.stop_event.is_set()

    @staticmethod
    def get_running_tasks():
        return schedule.get_jobs()

    @staticmethod
    def do(groups):
        for group in groups:
            logger.info(f"Scheduler : ordonne une requete pour le groupe {group}")
            try:
                request = requests_manager.create_request(group, 1)
                requests_manager.ask_for_request(request)
            except Exception as e:
                logger.error(f"Scheduler -> Requests Manager: Erreur lors de la demande de requete : {e}")

    def run_schedule(self):
        while not self.stop_event.is_set():
            logger.debug(f"Scheduler : en vie {self.schedule_thread.is_alive()}")
            schedule.run_pending()
            time.sleep(wait_time)

    def launch_scheduled(self):
        if self.stop_event.is_set():
            self.stop_event.clear()

            logger.info("Scheduler : lance les taches prévues")
            schedulers = Scheduler.objects.all()
            for scheduler in schedulers:
                if scheduler.all_time_running:
                    schedule.every(scheduler.refresh_time_min).minutes.do(
                        lambda: self.do(scheduler.targeted_groups.all())
                    ).tag(scheduler.id)
                    logger.info(f"Scheduler lancé pour: {scheduler.targeted_groups.all()} "
                                f"toutes les {scheduler.refresh_time_min} min")

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
