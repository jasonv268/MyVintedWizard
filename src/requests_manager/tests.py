import time

from django.test import TestCase
from loguru import logger

from requests_manager import interface as requests_manager
from requests_manager.tasks.requests_manager import requestsmg


# Create your tests here.

class RequestsManagerTest(TestCase):

    def setUp(self):
        requests_manager.init(2, 60)
        requests_manager.launch()

    def tearDown(self):
        requests_manager.stop()
        time.sleep(2)

    def test_1(self):
        logger.info("TEST 1 LANCE")
        start = time.time()
        requests_manager.ask_for_request(("g", 0))
        requests_manager.ask_for_request(("g", 0))
        while len(requestsmg.queue) > 0:
            time.sleep(2)
        delta_time = time.time() - start
        logger.info(f"requetes executées en {delta_time} s")
        self.assertLess(delta_time, 20)

    def test_2(self):
        logger.info("TEST 2 LANCE")
        start = time.time()
        requests_manager.ask_for_request(("g", 0))
        requests_manager.ask_for_request(("g", 0))
        requests_manager.ask_for_request(("g", 0))
        while len(requestsmg.queue) > 0:
            time.sleep(2)
        delta_time = time.time() - start
        logger.info(f"requetes executées en {delta_time} s")
        self.assertLess(delta_time, 70)

    def test_3(self):
        logger.info("TEST 3 LANCE")
        start = time.time()
        requests_manager.ask_for_request(("g", 0))
        time.sleep(59)
        requests_manager.ask_for_request(("g", 0))
        requests_manager.ask_for_request(("g", 0))
        while len(requestsmg.queue) > 0:
            time.sleep(2)
        delta_time = time.time() - start
        logger.info(f"requetes executées en {delta_time} s")
        self.assertLess(delta_time, 72)

    def test_4(self):
        logger.info("TEST 4 LANCE")
        start = time.time()
        requests_manager.ask_for_request(("g", 0))
        requests_manager.ask_for_request(("g", 0))
        requests_manager.ask_for_request(("g", 0))
        requests_manager.ask_for_request(("g", 0))
        while len(requestsmg.queue) > 0:
            time.sleep(2)
        delta_time = time.time() - start
        logger.info(f"requetes executées en {delta_time} s")
        self.assertLess(delta_time, 74)
