import matplotlib.pyplot as plt
import streamlit as st

def plot_total_cases(df):
    df_total = df[['Country/Region', 'Confirmed', 'Deaths', 'Recovered']].groupby('Country/Region').sum().reset_index()
    plt.figure(figsize=(10, 4))
    plt.bar(df_total['Country/Region'], df_total['Confirmed'], label='Confirmed', color='blue')
    plt.bar(df_total['Country/Region'], df_total['Deaths'], bottom=df_total['Confirmed'], label='Deaths', color='red')
    plt.bar(df_total['Country/Region'], df_total['Recovered'], bottom=df_total['Confirmed'] + df_total['Deaths'], label='Recovered', color='green')
    plt.xlabel('Country/Region')
    plt.ylabel('Number of Cases')
    plt.title('Total Confirmed, Deaths, and Recovered Cases')
    plt.savefig('plot_total_cases.png')
    return plt.gcf()

def plot_top_countries(df):
    df_top = df[['Country/Region', 'Confirmed']].groupby('Country/Region').sum().nlargest(10, 'Confirmed').reset_index()
    plt.figure(figsize=(10, 4))
    plt.bar(df_top['Country/Region'], df_top['Confirmed'], color='blue')
    plt.xlabel('Country/Region')
    plt.ylabel('Number of Confirmed Cases')
    plt.title('Top 10 Countries with the Highest Number of Confirmed Cases')
    plt.savefig('plot_top_countries.png')
    return plt.gcf()

def plot_daily_cases(df):
    if 'New cases' not in df.columns:
        raise ValueError("The DataFrame does not contain a 'New cases' column.")
    
    plt.figure(figsize=(10, 4))
    plt.pie(df['New cases'], labels=df['Country/Region'], autopct='%1.1f%%')
    plt.title('Daily New cases')
    plt.savefig('plot_daily_cases.png')
    return plt.gcf()
