import pandas as pd


def get_mean_on(df, target_column, time_frequency_in_h):
    df['scrap_date'] = pd.to_datetime(df['scrap_date'])
    # Grouper par intervalle d'une heure
    grouped_df = df.groupby(pd.Grouper(key='scrap_date', freq=str(time_frequency_in_h) + 'H')).mean(numeric_only=True)

    grouped_df = grouped_df.dropna()

    return grouped_df.index, grouped_df[target_column]


def get_columns(df, target_column_x=None, target_column_y=None):
    match (target_column_x, target_column_y):
        case (None, None):
            return None, None
        case (None, _):
            return None, df[target_column_y]
        case (_, None):
            return df[target_column_x], None
        case (_, _):
            return df[target_column_x], df[target_column_y]


def price_filtered_on_size(df):
    return [size for size in df['size'].unique()], [df[df['size'] == size]['price'].values for size in
                                                    df['size'].unique()]


def get_median_on(df, target_column, time_frequency_in_h):
    df['scrap_date'] = pd.to_datetime(df['scrap_date'])
    # Grouper par intervalle d'une heure
    grouped_df = df.groupby(pd.Grouper(key='scrap_date', freq=str(time_frequency_in_h) + 'H')).median(numeric_only=True)

    grouped_df = grouped_df.dropna()

    return grouped_df.index, grouped_df[target_column]


def get_grouped_by(df, gp_column, target_column, mode):
    gp = df.groupby(gp_column).describe()
    return gp.index, gp[target_column][mode]
