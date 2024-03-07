import os
import time
from pathlib import Path

import pandas as pd
from django.test import TestCase

from scraper.engine.files_manager import saver

# Create your tests here.
save_path = Path("scraper/tests_data/")


class FilesManagerTest(TestCase):

    def setUp(self):
        saver.save_path = save_path
        try:
            os.mkdir(save_path)
        except FileExistsError:
            pass
        finally:
            for dirs in os.listdir(save_path):
                for files in os.listdir(save_path / dirs):
                    os.remove(save_path / dirs / files)

    def tearDown(self):
        pass
        for dirs in os.listdir(save_path):
            for files in os.listdir(save_path / dirs):
                os.remove(save_path / dirs / files)

    def test_1(self):
        data = [
            {
                'id': 1,
                'username': 'warren9278',
                'price': 80.0,
                'likes': 0,
                'size': 'M',
                'brand': 'Nike',
                'title': 'Veste sans manche vintage nike - Taille "M"',
                'img_link': 'https://',
                'link': 'https://',
                'scrap_date': '2024-02-14 15:55:27'
            },
            {
                'id': 2,
                'username': 'alexisprtlss',
                'price': 70.0,
                'likes': 0,
                'size': 'M',
                'brand': 'Nike',
                'title': 'Maillot PSG 2013 Beckham 32',
                'img_link': 'https://',
                'link': 'https://',
                'scrap_date': '2024-02-14 15:55:27'
            },
            {
                'id': 3,
                'username': 'rete5678',
                'price': 82.0,
                'likes': 0,
                'size': 'XS',
                'brand': 'Nike',
                'title': 'Survêtement Nike tech',
                'img_link': 'https://',
                'link': 'https://',
                'scrap_date': '2024-02-12 15:55:27'
            }]
        df1 = pd.DataFrame(data)

        saver.add_dataframe(df1, -1)

        self.assertEqual(len(saver.load_first_dataframe(-1)), 3)

        data = [
            {
                'id': 4,
                'username': 'warren9278',
                'price': 80.0,
                'likes': 0,
                'size': 'M',
                'brand': 'Nike',
                'title': 'Veste sans manche vintage nike - Taille "M"',
                'img_link': 'https://',
                'link': 'https://',
                'scrap_date': '2024-02-14 15:55:27'
            }
        ]

        df2 = pd.DataFrame(data)

        time.sleep(2)
        saver.add_dataframe(df2, -1)

        self.assertEqual(len(saver.load_first_dataframe(-1)), 1)

        data = [
            {
                'id': 3,
                'username': 'warren9278',
                'price': 80.0,
                'likes': 10,
                'size': 'M',
                'brand': 'Nike',
                'title': 'Veste sans manche vintage nike - Taille "M"',
                'img_link': 'https://',
                'link': 'https://',
                'scrap_date': '2024-02-14 17:55:27'
            },
            {
                'id': 4,
                'username': 'warren9278',
                'price': 80.0,
                'likes': 15,
                'size': 'M',
                'brand': 'Nike',
                'title': 'Veste sans manche vintage nike - Taille "M"',
                'img_link': 'https://',
                'link': 'https://',
                'scrap_date': '2024-02-14 17:55:27'
            }
        ]

        df3 = pd.DataFrame(data)

        time.sleep(2)

        saver.add_dataframe(df3, -1)

        self.assertEqual(len(saver.load_first_dataframe(-1)), 1)

    def test_2(self):

        for dirs in os.listdir(save_path):
            for files in os.listdir(save_path / dirs):
                os.remove(save_path / dirs / files)

        data = [
            {
                'id': 1,
                'username': 'warren9278_prev',
                'price': 80.0,
                'likes': 0,
                'size': 'M',
                'brand': 'Nike',
                'title': 'Veste sans manche vintage nike - Taille "M"',
                'link': 'https://',
                'img_link': 'https://',
                'scrap_date': '2024-02-14 17:55:27'
            }
        ]

        df = pd.DataFrame(data)

        saver.add_dataframe(df, -1)

        self.assertEqual(len(saver.load_first_dataframe(-1)), 1)

        time.sleep(2)

        data = [
            {
                'id': 1,
                'username': 'warren9278',
                'price': 80.0,
                'likes': 0,
                'size': 'M',
                'brand': 'Nike',
                'title': 'Veste sans manche vintage nike - Taille "M"',
                'img_link': 'https://',
                'link': 'https://',
                'scrap_date': '2024-02-14 17:55:27'
            },
            {
                'id': 2,
                'username': 'warren9278',
                'price': 80.0,
                'likes': 0,
                'size': 'M',
                'brand': 'Nike',
                'title': 'Veste sans manche vintage nike - Taille "M"',
                'img_link': 'https://',
                'link': 'https://',
                'scrap_date': '2024-02-14 17:55:27'
            }
        ]

        df2 = pd.DataFrame(data)

        saver.add_dataframe(df2, -1)

        self.assertEqual(len(saver.load_first_dataframe(-1)), 1)

    def test_3(self):

        for dirs in os.listdir(save_path):
            for files in os.listdir(save_path / dirs):
                os.remove(save_path / dirs / files)

        data = [
            {
                'id': 1,
                'username': 'warren9278',
                'price': 80.0,
                'likes': 0,
                'size': 'M',
                'brand': 'Nike',
                'title': 'Veste sans manche vintage nike - Taille "M"',
                'img_link': 'https://',
                'link': 'https://',
                'scrap_date': '2024-02-14 17:55:27'
            }
        ]

        df = pd.DataFrame(data)

        saver.add_dataframe(df, -1)

        self.assertEqual(len(saver.load_first_dataframe(-1)), 1)

        time.sleep(2)

        data = [
            {
                'id': 1,
                'username': 'warren9278',
                'price': 80.0,
                'likes': 0,
                'size': 'M',
                'brand': 'Nike',
                'title': 'Veste sans manche vintage nike - Taille "M"',
                'img_link': 'https://',
                'link': 'https://',
                'scrap_date': '2024-02-14 17:55:27'
            }
        ]

        df2 = pd.DataFrame(data)

        time.sleep(2)

        saver.add_dataframe(df2, -1)

        self.assertEqual(len(saver.load_first_dataframe(-1)), 1)
