from discord_manager.tasks.discord_webhook_manager import discordwh


def start_sender():
    """
    Démarre l'envoi de messages Discord.

    Raises:
        Exception: En cas d'échec du démarrage de l'envoi de messages Discord.

    Returns:
        None
    """
    try:
        discordwh.start_sender()
    except Exception as e:
        # Gérer l'exception
        raise Exception(
            "Une erreur s'est produite lors du démarrage de l'envoi de messages Discord : {}".format(str(e)))


def stop_sender():
    """
    Arrête l'envoi de messages Discord.

    Raises:
        Exception: En cas d'échec de l'arrêt de l'envoi de messages Discord.

    Returns:
        None
    """
    try:
        discordwh.stop_sender()
    except Exception as e:
        # Gérer l'exception
        raise Exception("Une erreur s'est produite lors de l'arrêt de l'envoi de messages Discord : {}".format(str(e)))


def send(content):
    """
    Envoie un message Discord.

    Args:
        content (str): Le contenu du message à envoyer.

    Raises:
        Exception: En cas d'échec de l'envoi du message Discord.

    Returns:
        None
    """
    try:
        discordwh.send(content)
    except Exception as e:
        # Gérer l'exception
        raise Exception("Une erreur s'est produite lors de l'envoi du message Discord : {}".format(str(e)))
