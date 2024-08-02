import pandas as pd
from exceptions_saksham import DataCleaningError

def clean_data(file_path):
    try:
        
        df = pd.read_csv(file_path)

        df.fillna(df.mean(), inplace=True)

        df['Date'] = pd.to_datetime(df['Date'])
        
        df['Country'] = df['Country'].str.strip()

        return df
    except Exception as e:
        raise DataCleaningError("Error cleaning data: {}".format(e))


df = clean_data('clean_covid_data.csv')