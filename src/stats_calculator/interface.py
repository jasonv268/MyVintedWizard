from stats_calculator.calc import analyser


def get_analysed_data(group):
    """
    Obtient les données analysées pour un groupe spécifié.

    Args:
        group (str): Le nom ou l'identifiant du groupe pour lequel les données doivent être analysées.

    Returns:
        dict: Un dictionnaire contenant les résultats de l'analyse pour le groupe spécifié.
              Les clés du dictionnaire représentent les mesures ou les statistiques analysées,
              et les valeurs correspondent aux résultats de l'analyse.

    Raises:
        ValueError: Si le groupe spécifié n'existe pas ou si aucune donnée n'est disponible pour le groupe.

    Cette fonction utilise le module stats_calculator pour analyser les données du groupe spécifié.
    Les statistiques calculées comprennent la moyenne, l'écart type, la valeur minimale, la valeur maximale
    et la médiane des données du groupe.
    """
    try:
        return analyser.get_analysed_data(group)
    except ValueError as e:
        raise ValueError(f"Erreur lors de l'analyse des données pour le groupe '{group}': {e}")
    except Exception as e:
        raise RuntimeError(f"Erreur inattendue lors de l'analyse des données pour le groupe '{group}': {e}")
