import signal
import sys
import threading

from loguru import logger

from requests_manager import interface as requests_manager

from discord_manager import interface as discord_manager

from scheduler import interface as scheduler


def stop():
    requests_manager.stop()

    discord_manager.stop_all()

    for thread in threading.enumerate():
        logger.error(f"Thread encore en vie après stop : {thread.name}")


def launch():
    try:
        def signal_handler(*args):
            # Code to be executed on script closure
            logger.info("Demande arret du script")
            scheduler.stop_scheduled()
            requests_manager.stop()
            discord_manager.stop_all()
            logger.info("Signaux d'arrets envoyés")
            for thread in threading.enumerate():
                logger.error(f"Thread encore en vie après stop : {thread.name}")
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C
        signal.signal(signal.SIGTERM, signal_handler)

        requests_manager.launch()

    except Exception as e:
        raise Exception(f"Une erreur s'est produite lors du lancement des services : {str(e)}")
