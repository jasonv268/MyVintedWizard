import time

from django.test import TestCase
from loguru import logger

from requests_manager import interface as requests_manager
from requests_manager.tasks.requests_manager import requestsmg

import django

import services


# Create your tests here.

class RequestsManagerTest(django.test.TransactionTestCase):

    def setUp(self):
        requests_manager.reinit(2, 60)
        requests_manager.launch()

    def tearDown(self):
        requests_manager.stop()
        services.stop()
        time.sleep(2)

    @staticmethod
    def createGroup():

        from filters_manager.models import Group, Filter

        filter = Filter.objects.create(name="FTest", search_text="test")

        group = Group.objects.create(name="Test")
        group.filters.set([filter])

        return group

    @staticmethod
    def deleteGroup(id):

        from filters_manager.models import Group

        Group.objects.get(pk=id).delete()

    @staticmethod
    def increaseDeltaScrapNumber(number):
        requestsmg.config_dict["current_delta_requests_number"] += number

    @staticmethod
    def resetDeltaScrapNumber():
        requestsmg.config_dict["current_delta_requests_number"] = 0

    @staticmethod
    def getDeltaScrapNumber():
        return requestsmg.config_dict["current_delta_requests_number"]

    def test_1(self):
        logger.info("TEST 1 LANCE")

        group1 = self.createGroup()
        group2 = self.createGroup()

        r1 = requests_manager.create_request(group1, 0)
        r2 = requests_manager.create_request(group2, 0)

        start = time.time()

        requests_manager.ask_for_request(r1)
        requests_manager.ask_for_request(r2)

        while len(requestsmg.queue) > 0:
            time.sleep(2)

        delta_time = time.time() - start

        logger.info(f"requetes executées en {delta_time} s")

        self.assertLess(delta_time, 20)

    def test_2(self):
        logger.info("TEST 2 LANCE")

        group1 = self.createGroup()
        group2 = self.createGroup()
        group3 = self.createGroup()

        r1 = requests_manager.create_request(group1, 0)
        r2 = requests_manager.create_request(group2, 0)
        r3 = requests_manager.create_request(group3, 0)

        start = time.time()

        requests_manager.ask_for_request(r1)
        requests_manager.ask_for_request(r2)

        while len(requestsmg.queue) > 0:
            time.sleep(1)

        self.assertEquals(self.getDeltaScrapNumber(), 0)
        self.increaseDeltaScrapNumber(2)
        self.assertEquals(self.getDeltaScrapNumber(), 2)

        time.sleep(1)
        requests_manager.ask_for_request(r3)

        while len(requestsmg.queue) > 0:
            time.sleep(2)

        delta_time = time.time() - start

        logger.info(f"requetes executées en {delta_time} s")

        self.assertLess(delta_time, 72 + 6)
        self.assertGreater(delta_time, 60)

    def test_3(self):
        logger.info("TEST 3 LANCE")

        start = time.time()

        r1 = requests_manager.create_request(self.createGroup(), 0)
        requests_manager.ask_for_request(r1)

        while len(requestsmg.queue) > 0:
            time.sleep(1)

        self.assertEquals(self.getDeltaScrapNumber(), 0)
        self.increaseDeltaScrapNumber(2)
        self.assertEquals(self.getDeltaScrapNumber(), 2)

        time.sleep(59)

        r1 = requests_manager.create_request(self.createGroup(), 0)
        r2 = requests_manager.create_request(self.createGroup(), 0)
        requests_manager.ask_for_request(r1)
        requests_manager.ask_for_request(r2)

        self.assertEquals(self.getDeltaScrapNumber(), 0)

        while len(requestsmg.queue) > 0:
            time.sleep(2)

        delta_time = time.time() - start

        logger.info(f"requetes executées en {delta_time} s")

        self.assertLess(delta_time, 78 + 2)
        self.assertGreater(delta_time, 63)

    def test_4(self):
        logger.info("TEST 4 LANCE")
        start = time.time()

        r1 = requests_manager.create_request(self.createGroup(), 0)

        requests_manager.ask_for_request(r1)
        requests_manager.ask_for_request(r1)

        while len(requestsmg.queue) > 0:
            time.sleep(1)

        self.assertEquals(self.getDeltaScrapNumber(), 0)
        self.increaseDeltaScrapNumber(2)
        self.assertEquals(self.getDeltaScrapNumber(), 2)

        requests_manager.ask_for_request(r1)
        requests_manager.ask_for_request(r1)

        while len(requestsmg.queue) > 0:
            time.sleep(2)

        delta_time = time.time() - start
        logger.info(f"requetes executées en {delta_time} s")
        self.assertLess(delta_time, 82 + 2)
        self.assertGreater(delta_time, 64)
