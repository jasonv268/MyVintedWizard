from notifier.utils import notifier


def notify(request_id, dataframe):
    """
    Envoie une notification pour une demande spécifique avec un DataFrame donné.

    Cette fonction envoie une notification pour une demande identifiée par `request_id` avec les données spécifiées dans le DataFrame `dataframe`. La notification est envoyée en utilisant le module `notifier.utils`.

    Args:
        request_id (int): L'identifiant unique de la demande pour laquelle la notification est envoyée.
        dataframe (pandas.DataFrame): Le DataFrame contenant les données à inclure dans la notification.

    Returns:
        None

    Raises:
        ValueError: Si `request_id` est invalide ou si `dataframe` est vide.

    """
    try:
        notifier.notify(request_id, dataframe)
    except Exception as e:
        raise Exception("Une erreur s'est produite lors de l'envoi de notifications : {}".format(str(e)))
