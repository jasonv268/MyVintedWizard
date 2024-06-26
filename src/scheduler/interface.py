from scheduler.tasks.scheduler import schedulermg


def launch_scheduled():
    """
    Lance l'exécution des tâches planifiées.

    Raises:
        Exception: En cas d'échec du lancement des tâches planifiées.

    Returns:
        None
    """
    try:
        schedulermg.launch_scheduled()
    except Exception as e:
        # Gérer l'exception
        raise Exception("Une erreur s'est produite lors du lancement des tâches planifiées : {}".format(str(e)))


def stop_scheduled():
    """
    Arrête l'exécution des tâches planifiées.

    Raises:
        Exception: En cas d'échec de l'arrêt des tâches planifiées.

    Returns:
        None
    """
    try:
        schedulermg.stop_scheduled()
    except Exception as e:
        # Gérer l'exception
        raise Exception("Une erreur s'est produite lors de l'arrêt des tâches planifiées : {}".format(str(e)))


def is_running():
    """
    Arrête l'exécution des tâches planifiées.

    Raises:
        Exception: En cas d'échec de l'arrêt des tâches planifiées.

    Returns:
        True si le scheduler est actif
    """
    try:
        return schedulermg.is_running()
    except Exception as e:
        # Gérer l'exception
        raise Exception("Une erreur s'est produite lors de la demande : {}".format(str(e)))


def get_running_tasks():
    """
    Retourne les tâches planifiées.

    Raises:
        Exception: .

    Returns:
        La liste des taches planifiées
    """
    try:
        return schedulermg.get_running_tasks()
    except Exception as e:
        # Gérer l'exception
        raise Exception("Une erreur s'est produite lors de la demande : {}".format(str(e)))
