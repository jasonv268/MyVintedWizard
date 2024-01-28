import pandas as pd
import os

import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.offline as pyo

path = "stats_manager/ressources/data/"


def laod_dataframes(ide):
    files = os.listdir(path + str(ide))

    table = dict()

    for file in sorted(files):
        df = pd.read_csv(path + str(ide) + '/' + file)
        table[file.replace('.csv','')] = df

    return table


def get_concated_dataframe(dfs):
    total = pd.DataFrame()

    for v in dfs:
        # df = pd.read_csv(path + str(ide) + '/' + file)
        total = pd.concat([total, v], axis=0, ignore_index=True)

    return total


def clean_data_frame(df: pd.DataFrame):
    df = df[df['price'] != "NotFound"]
    df.price = df.price.astype(float)
    return df


def get_analysed_data(ide):
    dfs = laod_dataframes(ide).values()
    df_total = clean_data_frame(get_concated_dataframe(dfs))
    df_total = df_total.drop_duplicates(subset='id', keep='first')
    print(df_total['price'].median())
    data = dict()
    data['mean'] = get_mean(df_total)
    data['gmean'] = get_mean_grouped(df_total)
    data['html'] = write_html(ide, laod_dataframes(ide))
    return data


def get_mean(df: pd.DataFrame):
    return df['price'].mean()


def get_mean_grouped(df: pd.DataFrame):
    g = df.groupby(["size"]).price.mean()
    return {k: v for k, v in g.items()}


def write_html(ide, dfs):
    data = {'X': dfs.keys(),
            'Y': [get_mean(clean_data_frame(df)) for df in dfs.values()]}
    df = pd.DataFrame(data)



    # Créer un graphe Matplotlib
    plt.plot(df['X'], df['Y'])
    plt.title('Graph Matplotlib')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Conversion du graphique Matplotlib en Plotly
    fig = make_subplots()
    trace = go.Scatter(x=df['X'], y=df['Y'], mode='lines', name='Matplotlib Line')
    fig.add_trace(trace)
    fig.update_layout(
        autosize=True,
    )

    # Affichage du graphique Plotly dans une page HTML
    html_code = pyo.plot(fig, output_type='div')

    return html_code
