import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv(r"C:\Users\garvi\Downloads\clean_covid_data.csv")

df.reset_index(inplace=True)

st.sidebar.header('Filter Options')


start_idx, end_idx = st.sidebar.slider(
    'Select record range',
    min_value=0,
    max_value=len(df) - 1,
    value=(0, len(df) - 1)
)

countries = st.sidebar.multiselect('Select countries/states', df['Country/Region'].unique())
case_type = st.sidebar.selectbox('Select case type', ['Confirmed', 'Deaths', 'Recovered'])

filtered_df = df[(df['index'] >= start_idx) & (df['index'] <= end_idx)]
if countries:
    filtered_df = filtered_df[filtered_df['Country/Region'].isin(countries)]


df_grouped = filtered_df.groupby('Country/Region').sum().reset_index()


plt.clf()
plt.figure(figsize=(10, 6))
plt.plot(df_grouped['Country/Region'], df_grouped[case_type], label=case_type, color='blue')
plt.xlabel('Country/Region')
plt.ylabel('Number of Cases')
plt.title('Total ' + case_type + ' Cases by Country')
plt.legend()
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(plt)