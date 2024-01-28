import time

from django.core.cache import cache
from django.shortcuts import get_object_or_404

from stats_manager.utils.scraping import scraper
from stats_manager.utils.analysing import analyser

from filters_manager.models import Group


class StatsManager:
    path_data = "stats_manager/ressources/data/"

    def __init__(self, requests_number, delta_time):
        cache.add('init_time', time.time())
        cache.add('last_scrap_time', time.time() - delta_time)
        cache.add('total_scrap', 0)

        self.requests_number = requests_number
        self.delta_time = delta_time

    def reinit(self):
        cache.set('first_scrap', time.time())
        cache.set('last_scrap', time.time() - self.delta_time)
        cache.set('total_scrap', 0)

    def requests(self, group):
        current_time = time.time()
        if current_time - cache.get('last_scrap_time') >= self.delta_time:
            cache.set('last_scrap_time', current_time)
            urls = []
            for filter in group.filters.all():
                urls.append((filter.id, filter.get_full_url()))
            scraper.start_scraping(urls, 3)
            cache.set('total_scrap', cache.get('total_scrap')+3)

    def analyses(self, group):

        try:

            data = analyser.get_analysed_data(group.filters.all()[0].id)
            return data

        except:

            return {}
