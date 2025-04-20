import pandas as pd

def preprocess_input(data):
    """
    Transforms input dict with 'date_time' and 'junction' into model features:
    ['hour', 'day_of_week', 'month', 'Junction']
    """
    df = pd.DataFrame([data])
    df['date_time'] = pd.to_datetime(df['date_time'])

    df['hour'] = df['date_time'].dt.hour
    df['day_of_week'] = df['date_time'].dt.weekday
    df['month'] = df['date_time'].dt.month
    df['Junction'] = df['junction']

    return df[['hour', 'day_of_week', 'month', 'Junction']]
