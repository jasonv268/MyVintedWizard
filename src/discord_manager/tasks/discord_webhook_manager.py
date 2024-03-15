import os
import threading
import time
import json

from loguru import logger
import discord

from notifier.utils.Notif import Notif


class DiscordWebHookManager:
    def __init__(self):
        self.webhooks: list[DiscordWebHook] = []

    def add_web_hook(self, channel_url):
        webhook = DiscordWebHook(channel_url)
        self.webhooks.append(webhook)
        return webhook

    def stop_all(self):
        for webhook in self.webhooks:
            webhook.stop_sender()


class DiscordWebHook:

    def __init__(self, channel_url):
        self.webhook = discord.SyncWebhook.from_url(channel_url)
        self.queue = []
        self.notify_event = threading.Event()
        self.stop_event = threading.Event()
        self.stop_event.set()
        self.thread = threading.Thread(target=self.sender)

    def send(self, content):
        self.queue.append(content)
        logger.info(f"WEBHOOK a ajouté à la queue {content}")
        self.notify_event.set()

    def start_sender(self):
        if self.stop_event.is_set():
            self.stop_event.clear()
            self.notify_event.set()
            self.thread = threading.Thread(target=self.sender)
            self.thread.start()
            logger.info(f"WEBHOOK: sender lancé")

    def stop_sender(self):
        logger.info(f"WEBHOOK: stop flag envoyé au sender")
        if not self.stop_event.is_set():
            self.stop_event.set()
            self.notify_event.set()
            logger.info(f"WEBHOOK: sender arreté")

    def sender(self):

        def format_content(c):
            attr = json.loads(c)
            o = Notif.deserialize(attr)
            return o.get_embed()

        while not self.stop_event.is_set():
            logger.info("WEBHOOK en attente pour économiser les ressources")
            self.notify_event.wait()  # Attendre jusqu'à ce qu'un nouveau message soit disponible
            logger.info("WEBHOOK en action")
            if self.queue:
                while len(self.queue) > 0:
                    content = self.queue.pop(0)

                    embed_content = format_content(content)

                    try:
                        self.webhook.send(embed=embed_content)
                        logger.info(f"WEBHOOK a envoyé {content}")
                    except discord.errors.HTTPException:
                        self.webhook.send("ERREUR")
                        logger.info(f"WEBHOOK a envoyé ERREUR")
                    self.notify_event.clear()
                    time.sleep(2)  # Attendre 2 secondes avant d'envoyer le prochain message
            self.notify_event.clear()


discordmg = DiscordWebHookManager()
