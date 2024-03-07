import time

from django.test import TestCase
import pandas as pd

from notifier.utils import notifier

from notifier.models import Notifier


class NotifierTest(TestCase):

    def setUp(self):
        Notifier.objects.create(name="test1", price_min=1.01, price_max=70, algo_filtrage=True, mode_tri="PRICEASC")
        Notifier.objects.create(name="test2", price_min=1.01, price_max=80, algo_filtrage=True, mode_tri="PRICEASC")

    def test_1(self):
        data = [
            {
                'id': 4101171365,
                'username': 'warren9278',
                'price': 80.0,
                'likes': 0,
                'size': 'M',
                'brand': 'Nike',
                'title': 'Veste sans manche vintage nike - Taille "M"',
                'img_link': 'https://images1.vinted.net/t/03_0258f_sUHEfsUWMBZnHLSmkzBxoUjG/310x430/1708185427.jpeg?s=62ea98dbe5c772185649a437ce4e21ebf7a9bacd',
                'link': 'https://www.vinted.fr/items/4112057125-parachute-baggy-pants-nike-black?referrer=catalog',
                'scrap_date': '2024-02-14 15:55:27'
            },
            {
                'id': 4101086457,
                'username': 'alexisprtlss',
                'price': 70.0,
                'likes': 0,
                'size': 'M',
                'brand': 'Nike',
                'title': 'Maillot PSG 2013 Beckham 32',
                'img_link': 'https://images1.vinted.net/t/03_0258f_sUHEfsUWMBZnHLSmkzBxoUjG/310x430/1708185427.jpeg?s=62ea98dbe5c772185649a437ce4e21ebf7a9bacd',
                'link': 'https://www.vinted.fr/items/4112057125-parachute-baggy-pants-nike-black?referrer=catalog',
                'scrap_date': '2024-02-14 15:55:27'
            },
            {
                'id': 4100962063,
                'username': 'rete5678',
                'price': 82.0,
                'likes': 11,
                'size': 'XS',
                'brand': 'Nike',
                'title': 'Survêtement Nike tech',
                'img_link': 'https://images1.vinted.net/t/03_0258f_sUHEfsUWMBZnHLSmkzBxoUjG/310x430/1708185427.jpeg?s=62ea98dbe5c772185649a437ce4e21ebf7a9bacd',
                'link': 'https://www.vinted.fr/items/4112057125-parachute-baggy-pants-nike-black?referrer=catalog',
                'scrap_date': '2024-02-12 15:55:27'
            }]
        df1 = pd.DataFrame(data)
        notifier.send_all(df1, Notifier.objects.get(id=1))

        time.sleep(5)

        notifier.send_all(df1, Notifier.objects.get(id=2))


