from loguru import logger

from filters_manager.models import Filter
from discord_manager import interface as discordwh
from notifier.utils.Notif import Notif
from notifier.utils import helpers


def notify(ide, df):
    logger.info(f"Notifier : Recherche notifier sur filtre d'id {ide}")
    if df.shape[0] > 0:
        f = Filter.objects.get(id=ide)
        if f.notifier is not None:
            notifier = f.notifier
            logger.info(f"Notifier : notifier trouvé sur filtre")
            logger.info(f"Notifier : Envoie notifs")
            send_all(df, notifier)
        else:
            logger.info(f"Notifier : pas de notifier associé au filtre")


def send_all(df, notifier):
    for index, row in df.iterrows():
        if helpers.check_all(notifier, row):
            notif = Notif(row['username'], row['price'], row['likes'], row['size'], row['brand'], row['title'],
                          row['img_link'], row['link'], row['scrap_date'])

            logger.info(f"Notifier : Send {notif.serialize()}")

            discordwh.send(notif.serialize())
