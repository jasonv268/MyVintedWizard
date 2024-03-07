import os
from datetime import datetime
from pathlib import Path

import pandas as pd
from loguru import logger

from notifier import interface as notifier

save_path = Path("scraper/ressources/data/")

pd.set_option("mode.copy_on_write", True)

data_types = {"id": "int64", "username": "string", "price": "float64", "likes": "int64", "size": "string",
              "brand": "string", "title": "string", "img_link": "string", "link": "string", "scrap_date": "string"}


def add_dataframe(scraped_data: pd.DataFrame, request_id):
    logger.info(f"Saver : ajout des données collectées pour le filtre {request_id}")

    print("AJOUT", scraped_data)

    current_path = save_path / str(request_id) / ""

    if not os.path.exists(current_path):
        os.makedirs(current_path, exist_ok=False)

    date = datetime.today().strftime('%Y-%m-%d %Hh%Mmin%Ssec')
    scraped_data["scrap_date"] = date

    scraped_data.dropna(inplace=True)
    scraped_data = scraped_data.astype(data_types)

    exists, previous_data = read_csvs_if_exists(request_id)

    if not exists:
        logger.info(f"Saver : Enregistrement des données dans un nouveau fichier")
        scraped_data.to_csv(current_path / Path(date + ".csv"), index=False)
        notifier.notify(request_id, scraped_data)

        print("NOT EXIST", scraped_data)

    else:
        logger.info(f"Saver : Enregistrement des données par concaténation dans un fichier existant")

        print("PREVIOUS", previous_data)

        scraped_data_minus_previous = scraped_data[~scraped_data['id'].isin(previous_data['id'])]

        print("NEW", scraped_data_minus_previous)

        if scraped_data_minus_previous.shape[0] > 0:
            notifier.notify(request_id=request_id, dataframe=scraped_data_minus_previous)
            scraped_data_minus_previous.to_csv(current_path / Path(date + ".csv"), index=False)


def read_csvs_if_exists(request_id):
    logger.info(f"Saver : Demande csv correspondant au filtre {request_id}")
    current_path = save_path / str(request_id) / ""
    total = pd.DataFrame()
    files = sorted(os.listdir(current_path), reverse=True)
    index = 0
    while total.shape[0] < 182 and index <= len(files) - 1:
        df = pd.read_csv(current_path / files[index])
        total = pd.concat([total, df], axis=0, ignore_index=True)
        index += 1
    if index == 0:
        return False, None
    else:
        return True, total


def load_dataframe(ide) -> pd.DataFrame:
    try:
        logger.info(f"Saver : Demande datframe correspondant au filtre {ide}")
        files = os.listdir(save_path / str(ide))
        df = pd.DataFrame()
        for file in files:
            df = pd.read_csv(save_path / str(ide) / file)
        return df

    except FileNotFoundError:
        return pd.DataFrame()

    finally:
        pass


def load_dataframes(ide) -> pd.DataFrame:
    try:
        logger.info(f"Saver : Demande datframes correspondant au filtre {ide}")
        current_path = save_path / str(ide) / ""
        total = pd.DataFrame()
        files = sorted(os.listdir(current_path), reverse=True)
        for file in files:
            df = pd.read_csv(current_path / file)
            total = pd.concat([total, df], axis=0, ignore_index=True)
        return total

    except FileNotFoundError:
        return pd.DataFrame()

    finally:
        pass


def load_first_dataframe(ide) -> pd.DataFrame:
    try:
        logger.info(f"Saver : Demande datframe correspondant au filtre {ide}")
        current_path = save_path / str(ide) / ""
        files = sorted(os.listdir(current_path), reverse=True)
        for file in files:
            df = pd.read_csv(save_path / str(ide) / file)
            print("LOAD FIRST", df)
            return df
        return pd.DataFrame()

    except FileNotFoundError:
        return pd.DataFrame()


def get_date(ide) -> str:
    try:
        files = os.listdir(save_path / str(ide))
        for file in files:
            return str(file.replace(".csv", "").replace("_", ""))
        return "Not Scraped"

    except FileNotFoundError:
        return "Not Scraped"
