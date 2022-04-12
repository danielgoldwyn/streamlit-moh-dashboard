from cProfile import label
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

icu_url = 'https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/icu.csv'

#get the raw data from MOH git repo
@st.cache(allow_output_mutation=True)
def fetch_data(url):
    return_data = pd.read_csv(url)
    return return_data


def main():

    #get sum from various series based on a given date
    def get_sum(date,val):
        return df_icu.loc[df_icu['date']==date, val].sum()

    # funtion to return the ratio
    def find_ratio(r_date, r_value):
        r = bar_chart_df.loc[r_date,r_value]/bar_chart_df.loc[r_date,'icu_covid']
        return f'{r:.0%}'

    #load data
    df_icu = fetch_data(icu_url)
    df_icu['date'] = pd.to_datetime(df_icu['date'])
    latest_date = df_icu['date'].drop_duplicates().nlargest(1).iloc[0]
    second_latest_date = df_icu['date'].drop_duplicates().nlargest(2).iloc[-1]

    # get the latest icu case
    latest_icu = get_sum(latest_date,'icu_covid')
    second_latest_icu = get_sum(second_latest_date, 'icu_covid')
    delta_icu = ((latest_icu-second_latest_icu)/second_latest_icu)*100

    # get the latest ventilator used
    latest_vent = get_sum(latest_date,'vent_covid')
    second_latest_vent = get_sum(second_latest_date, 'vent_covid')
    delta_vent = ((latest_vent-second_latest_vent)/second_latest_vent)*100

    #get the total ventilator
    total_vent = get_sum(latest_date, 'vent')

    #get the total icu bed
    total_icu = get_sum(latest_date, 'beds_icu_covid')

    #test pyplot
    past_week = df_icu['date'].drop_duplicates().nlargest(7)
    date_filt = df_icu.loc[(df_icu['date'] >= past_week.iloc[-1]) & (df_icu['date'] <= past_week.iloc[0])]

    barchart_df = date_filt[['date','icu_covid','vent_covid']]

    bar_chart_df = barchart_df.groupby(barchart_df['date'])[['icu_covid','vent_covid']].sum()
    bar_chart_df['no_vent'] = bar_chart_df['icu_covid'] - bar_chart_df['vent_covid']


    #START OF THE STREAMLIT WEBAPP
    st.title('ICU Stats of Malaysia Covid Cases')
    st.write('Proof of concept using python streamlit to create a dashboard compiling quick statistics from the Malaysian Ministry of Health Github repository')
    st.write(f"Data as of {latest_date:%d-%b-%Y} from Malaysian Ministry of Health Github repo")
    st.header('Quick view of daily ICU and Ventilator usage')
    col1, col2, col3, col4 = st.columns(4)

    col1.metric('ICU', latest_icu, f"{delta_icu:.2f}%", 'inverse')
    col2.metric('ICU Capacity', f"{latest_icu / total_icu * 100 :.0f}%" )
    col3.metric('Ventilator', latest_vent, f"{delta_vent:.2f}%", 'inverse')
    col4.metric('Vent Capacity', f"{latest_vent / total_vent * 100 :.0f}%" )


    st.header('7 day breakdown of ICU patients needing ventilators')
    fig, ax = plt.subplots()
    p1 = ax.bar(bar_chart_df.index.strftime('%d-%b'),bar_chart_df['vent_covid'], label="Need Vent")
    p2 = ax.bar(bar_chart_df.index.strftime('%d-%b'),bar_chart_df['no_vent'], bottom=bar_chart_df['vent_covid'], label="No Vent")
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Patients')
    #ax.set_title('7 day breakdown of ICU patients needing ventilators')
    ax.legend()

    ax.bar_label(p1, label_type='center', labels=[find_ratio(e,'vent_covid') for e in bar_chart_df.index])
    ax.bar_label(p2, label_type='center', labels=[find_ratio(e,'no_vent') for e in bar_chart_df.index])
    ax.bar_label(p2)
    st.pyplot(fig)

    st.write('*more features to be added soon')

if __name__ == '__main__':
    main()