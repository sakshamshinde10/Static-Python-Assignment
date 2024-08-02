import pandas as pd

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

def load_data(file_path):
    return pd.read_csv(file_path)