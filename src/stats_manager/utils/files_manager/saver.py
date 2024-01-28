from itertools import count

import pandas as pd
import os
from datetime import datetime
import json

save_path = "stats_manager/ressources/data/"


# nom dossier, on peut mettre l'id de la requete / le nom

def save_dataframe(df: pd.DataFrame, request_id):
    current_path = save_path + str(request_id) + "/"

    print("saver")

    if not os.path.exists(current_path):
        os.makedirs(current_path, exist_ok=False)

    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    df.to_csv(current_path + date + ".csv", index=False)


def load_dataframes(ide):
    current_path = save_path + ide + "/"
    f = []
    for (_, _, filenames) in os.walk(current_path):
        f.extend(filenames)

