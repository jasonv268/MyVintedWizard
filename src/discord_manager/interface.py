from discord_manager.tasks.discord_webhook_manager import discordmg
from discord_manager.tasks.discord_webhook_manager import DiscordWebHook


def add_sender(channel_url):
    """
    Démarre l'envoi de messages Discord.

    Raises:
        Exception: En cas d'échec du démarrage de l'envoi de messages Discord.

    Returns:
        None
    """
    try:
        return discordmg.add_web_hook(channel_url)
    except Exception as e:
        # Gérer l'exception
        raise Exception(
            "Une erreur s'est produite lors du démarrage de l'envoi de messages Discord : {}".format(str(e)))


def start_sender(webhook: DiscordWebHook):
    """
    Démarre l'envoi de messages Discord.

    Raises:
        Exception: En cas d'échec du démarrage de l'envoi de messages Discord.

    Returns:
        None
    """
    try:
        webhook.start_sender()
    except Exception as e:
        # Gérer l'exception
        raise Exception(
            "Une erreur s'est produite lors du démarrage de l'envoi de messages Discord : {}".format(str(e)))


def stop_sender(web_hook):
    """
    Arrête l'envoi de messages Discord.

    Raises:
        Exception: En cas d'échec de l'arrêt de l'envoi de messages Discord.

    Returns:
        None
    """
    try:
        web_hook.stop_sender()
    except Exception as e:
        # Gérer l'exception
        raise Exception("Une erreur s'est produite lors de l'arrêt de l'envoi de messages Discord : {}".format(str(e)))


def send(webhook: DiscordWebHook, content):
    """
    Envoie un message Discord.

    Args:
        webhook (DiscordWebHook): Le webhook utilisé
        content (str): Le contenu du message à envoyer.

    Raises:
        Exception: En cas d'échec de l'envoi du message Discord.

    Returns:
        None
    """
    try:
        webhook.send(content)
    except Exception as e:
        # Gérer l'exception
        raise Exception("Une erreur s'est produite lors de l'envoi du message Discord : {}".format(str(e)))


def stop_all():
    """
    Arrête l'envoi de messages Discord.

    Raises:
        Exception: En cas d'échec de l'arrêt de l'envoi de messages Discord.

    Returns:
        None
    """
    try:
        discordmg.stop_all()
    except Exception as e:
        # Gérer l'exception
        raise Exception("Une erreur s'est produite lors de l'arrêt de l'envoi de messages Discord : {}".format(str(e)))
