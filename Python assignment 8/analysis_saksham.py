import visualization_saksham 
import dashboard_saksham 
import filehandling_saksham 
import exceptions_saksham 
import data_cleaning_saksham

def main():
    df = filehandling_saksham.read_csv('country_wise_latest.csv')
    try:
        df = data_cleaning_saksham.clean_data(df)
        filehandling_saksham.write_csv('clean_covid_data.csv', df)
    except exceptions_saksham.DataCleaningError as e:
        print(f"Data cleaning error: {e.message}")
        return

    visualization_saksham.plot_total_cases(df)
    visualization_saksham.plot_top_countries(df)
    visualization_saksham.plot_daily_cases(df)

    dashboard_saksham.create_dashboard(df)  

main()