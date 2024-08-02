
import pandas as pd
import matplotlib.pyplot as plt
from exceptions_saksham import DataCleaningError

def analyze_data(file_path):
    try:
        
        data = pd.read_csv(file_path)
        print("Data columns:", data.columns.tolist())
        print("First few rows of data:\n", data.head())
        required_columns = ['Country/Region', 'Confirmed', 'Deaths', 'Recovered']
        for column in required_columns:
            if column not in data.columns:
                raise DataCleaningError(f"Missing required column: {column}")
            
        total_cases = data['Confirmed'].sum()
        total_deaths = data['Deaths'].sum()
        total_recovered = data['Recovered'].sum()
        
        print("Total Cases:", total_cases)
        print("Total Deaths:", total_deaths)
        print("Total Recovered:", total_recovered)
        

        top_countries = data.groupby('Country/Region')['Confirmed'].sum().sort_values(ascending=False).head(5)
        bottom_countries = data.groupby('Country/Region')['Confirmed'].sum().sort_values(ascending=True).head(5)
        
        print("Top 5 Countries by Cases:")
        print(top_countries)
        print("Bottom 5 Countries by Cases:")
        print(bottom_countries)
        
    
        plot_total_cases(data)
        
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except DataCleaningError as e:
        print(f"Data cleaning error: {e}")
    except pd.errors.EmptyDataError:
        print("No data found in the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def plot_total_cases(data):
    plt.figure(figsize=(10, 6))
    data['Total Cases'] = data['Confirmed'] + data['Deaths'] + data['Recovered']
    country_cases = data.groupby('Country/Region')['Total Cases'].sum().sort_values(ascending=False)
    country_cases.plot(kind='bar')
    plt.xlabel('Country/Region')
    plt.ylabel('Total Cases')
    plt.title('Total Cases by Country/Region')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


analyze_data('clean_covid_data.csv')
