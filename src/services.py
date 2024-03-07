import signal
import sys

from loguru import logger

from requests_manager import interface as requests_manager

from discord_manager import interface as discord_manager

from scheduler import interface as scheduler


def launch():
    try:
        def signal_handler(*args):
            # Code to be executed on script closure
            logger.info("Demande arret du script")
            scheduler.stop_scheduled()
            requests_manager.stop()
            discord_manager.stop_sender()
            logger.info("Signaux d'arrets envoyés")
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C
        signal.signal(signal.SIGTERM, signal_handler)

        requests_manager.launch()

        discord_manager.start_sender()

    except Exception as e:
        raise Exception(f"Une erreur s'est produite lors du lancement des services : {str(e)}")
