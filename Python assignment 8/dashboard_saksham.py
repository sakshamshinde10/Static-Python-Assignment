import streamlit as st
from visualization_saksham import plot_total_cases,plot_top_countries,plot_daily_cases

def create_dashboard(df):
    st.title('COVID-19 Data Visualization Dashboard')
    countries = st.multiselect('Country/Region', df['Country/Region'].unique())
    case_types = st.selectbox('Case Types', ['Confirmed', 'Deaths', 'Recovered'])
    if st.button('Visualize'):
        df_filtered = df
        if countries:
            df_filtered = df_filtered[df_filtered['Country/Region'].isin(countries)]

        fig1 = plot_total_cases(df_filtered)
        st.pyplot(fig1)
        fig2 = plot_top_countries(df_filtered)
        st.pyplot(fig2)
        fig3 = plot_daily_cases(df_filtered)
        st.pyplot(fig3)