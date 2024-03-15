import time

from django.test import TestCase
import pandas as pd

import services

from notifier.utils import notifier

from notifier.models import Notifier


class NotifierTest(TestCase):

    def setUp(self):
        services.launch()

        Notifier.objects.create(name="test1",
                                webhook_url="https://discord.com/api/webhooks/1210161827812478976/eg61-n6r2mDv5vKNH2ScP0hz7EPo-5kDjoL10kKqbrK_VKVDRpvGgK9kAaA2xfIWWjtH",
                                price_min=1.01, price_max=70, algo_filtrage=True, mode_tri="PRICEASC")
        Notifier.objects.create(name="test2",
                                webhook_url="https://discord.com/api/webhooks/1210161827812478976/eg61-n6r2mDv5vKNH2ScP0hz7EPo-5kDjoL10kKqbrK_VKVDRpvGgK9kAaA2xfIWWjtH",
                                price_min=1.01, price_max=80, algo_filtrage=True, mode_tri="PRICEASC")
        Notifier.objects.create(name="test3",
                                webhook_url="https://discord.com/api/webhooks/1210161827812478976/eg61-n6r2mDv5vKNH2ScP0hz7EPo-5kDjoL10kKqbrK_VKVDRpvGgK9kAaA2xfIWWjtH",
                                price_min=80, price_max=100, algo_filtrage=True, mode_tri="PRICEASC")

    def tearDown(self):
        time.sleep(5)
        services.stop()

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
                'img_link': 'https://www.vinted.fr/items/4112057125-parachute-baggy-pants-nike-black?referrer=catalog',
                'link': 'https://www.vinted.fr/items/4112057125-parachute-baggy-pants-nike-black?referrer=catalog',
                'scrap_date': '2024-02-12 15:55:27'
            }]
        df1 = pd.DataFrame(data)
        notifier.send_all(df1, Notifier.objects.get(id=1))

    def test_2(self):
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
                'img_link': 'https://www.vinted.fr/items/4112057125-parachute-baggy-pants-nike-black?referrer=catalog',
                'link': 'https://www.vinted.fr/items/4112057125-parachute-baggy-pants-nike-black?referrer=catalog',
                'scrap_date': '2024-02-12 15:55:27'
            }]
        df1 = pd.DataFrame(data)
        notifier.send_all(df1, Notifier.objects.get(id=2))

    def test_3(self):
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
                'img_link': 'https://www.vinted.fr/items/4112057125-parachute-baggy-pants-nike-black?referrer=catalog',
                'link': 'https://www.vinted.fr/items/4112057125-parachute-baggy-pants-nike-black?referrer=catalog',
                'scrap_date': '2024-02-12 15:55:27'
            }]
        df1 = pd.DataFrame(data)
        notifier.send_all(df1, Notifier.objects.get(id=3))
