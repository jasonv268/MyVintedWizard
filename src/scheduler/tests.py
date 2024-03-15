from django.test import TestCase

from scheduler import interface as schedulermg
from scheduler.models import Scheduler
from scheduler.tasks import scheduler

from filters_manager.models import Group
from filters_manager.models import Filter

import services


# Create your tests here.

class SchedulerTest(TestCase):

    def setUp(self):
        scheduler.wait_time = 2

    def tearDown(self):
        scheduler.wait_time = 60
        services.stop()

    @staticmethod
    def createScheduler():
        filter = Filter.objects.create(name="FTest", search_text="test")

        group = Group.objects.create(name="Test")

        group.filters.set([filter])

        scheduler_ = Scheduler.objects.create(refresh_time_min=1, all_time_running=True)

        scheduler_.targeted_groups.set([group])

        return scheduler_

    @staticmethod
    def deleteScheduler(id):
        Scheduler.objects.get(pk=id).delete()

    def test_1(self):
        scheduler1 = self.createScheduler()

        schedulermg.launch_scheduled()

        self.assertTrue(schedulermg.is_running())

        self.assertEquals(len(schedulermg.get_running_tasks()), 1)

        schedulermg.stop_scheduled()

        self.assertFalse(schedulermg.is_running())

    def test_2(self):
        schedulermg.launch_scheduled()

        self.assertTrue(schedulermg.is_running())

        self.assertEquals(schedulermg.get_running_tasks(), [])

        schedulermg.stop_scheduled()

        self.assertFalse(schedulermg.is_running())

    def test_3(self):
        scheduler1 = self.createScheduler()

        schedulermg.launch_scheduled()

        self.assertTrue(schedulermg.is_running())

        self.assertEquals(len(schedulermg.get_running_tasks()), 1)

        scheduler2 = self.createScheduler()

        self.assertEquals(len(schedulermg.get_running_tasks()), 1)

        schedulermg.stop_scheduled()

        self.assertFalse(schedulermg.is_running())

        schedulermg.launch_scheduled()

        self.assertTrue(schedulermg.is_running())

        self.assertEquals(len(schedulermg.get_running_tasks()), 2)

        self.deleteScheduler(scheduler2.id)

        self.assertEquals(len(schedulermg.get_running_tasks()), 2)

        schedulermg.stop_scheduled()

        self.assertFalse(schedulermg.is_running())

        schedulermg.launch_scheduled()

        self.assertTrue(schedulermg.is_running())

        self.assertEquals(len(schedulermg.get_running_tasks()), 1)

        schedulermg.stop_scheduled()

        self.assertFalse(schedulermg.is_running())
