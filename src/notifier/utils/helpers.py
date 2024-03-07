import json
from pathlib import Path

ban_words_path = Path("notifier/utils/ban_words.json")


def check_all(notifier, row):
    def price_check(price):
        if notifier.price_min is not None and notifier.price_max is not None:
            return notifier.price_min <= price <= notifier.price_max
        else:
            return True

    def likes_check(likes):
        if notifier.nb_like_min is not None and notifier.nb_like_max is not None:
            return notifier.nb_like_min <= likes <= notifier.nb_like_max
        else:
            return True

    def filter_check(title: str):
        if notifier.algo_filtrage:
            with open(ban_words_path) as ban_words:
                ban_words_dict = json.load(ban_words)
                for key, value in ban_words_dict.items():
                    if value and key.replace(" ", "") in title.lower().replace(" ", ""):
                        return False
            return True
        else:
            return True

    return price_check(row['price']) and likes_check(row['likes']) and filter_check(row['title'])
