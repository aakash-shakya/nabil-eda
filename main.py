'''
    EDA performed by aakash shakya
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st

st.set_page_config(
    page_title='Nabil share price EDA',
    page_icon='📈',
    initial_sidebar_state='expanded'
)

df = pd.read_csv('nepsealpha_export_price_NABIL_2013-01-26_2023-01-26.csv')

# streamlit sidebar
with st.sidebar:
    st.subheader('📈 Nabil Bank Share Price EDA 📈 `version 1.0`')

    dataframe_arr = ['Data Shape', 'Data Description table', 'Dataset Details table', 'Numerical Data Types', 'Categorical Data Types']
    visualization_arr = [ 'Heatmap of the correlation of the numerical values', 'Barplot of "Volume with respect to the year"', 'Lineplot of "Volume with respect to the year"', 'Lineplot of "Close with respect to the year"', 'Linechart of Close', 'Linechart of Volume']
    
    st.write('---')

    st.markdown('[___DataFrame___](#dataframe)')
    st.markdown(f'''<span style="color:green">●</span> [Data Shape](#data-shape) ''', unsafe_allow_html=True)
    st.markdown(f'''<span style="color:green">●</span> [Data Description table](#data-description-table) ''', unsafe_allow_html=True)
    st.markdown(f'''<span style="color:green">●</span> [Dataset Details table](#dataset-details-table) ''', unsafe_allow_html=True)
    st.markdown(f'''<span style="color:green">●</span> [Numerical Data Types](#numerical-data-types-in-the-dataframe) ''', unsafe_allow_html=True)
    st.markdown(f'''<span style="color:green">●</span> [Categorical Data Types](#categorical-data-types-in-the-dataframe) ''', unsafe_allow_html=True)

    # for i in dataframe_arr:
    #     st.markdown(f'''<span style="color:green">●</span> [{i}] ''', unsafe_allow_html=True)
    
    st.markdown('[___Visualizations___](#visualizations)')
    st.markdown(f'''<span style="color:red">●</span> [Heatmap of the correlation of the numerical values](#heatmap-of-the-correlation-of-the-numerical-values) ''', unsafe_allow_html=True)
    st.markdown(f'''<span style="color:red">●</span> [Barplot of ____"Volume with respect to the year"___](#barplot-of-volume-with-respect-to-the-year) ''', unsafe_allow_html=True)
    st.markdown(f'''<span style="color:red">●</span> [Lineplot of ____"Volume with respect to the year"___](#lineplot-of-volume-with-respect-to-the-year) ''', unsafe_allow_html=True)
    st.markdown(f'''<span style="color:red">●</span> [Lineplot of ___"Close with respect to the year"___](#lineplot-of-close-with-respect-to-the-year) ''', unsafe_allow_html=True)
    st.markdown(f'''<span style="color:red">●</span> [Linechart of ___Close___](#linechart-of-close) ''', unsafe_allow_html=True)
    st.markdown(f'''<span style="color:red">●</span> [Linechart of ___Volume___](#linechart-of-volume) ''', unsafe_allow_html=True)

    # for j in visualization_arr:
    #     st.markdown(f'''<span style="color:red">●</span> {j}''', unsafe_allow_html=True)

    # st.markdown('''Created with ❤️ by [aakas](https://aakas.com.np).''')

st.title("📈 Nabil Bank Share Price EDA 📈")
st.write('''
    The data has been taken from the nepsealpha website. The data is from  ___2013-01-26___ to ___2023-01-26___.
''')

st.write('---')
st.subheader('DataFrame')
st.dataframe(df.head(10))

st.write('---')
st.subheader('Data Shape')
st.subheader(df.shape)

st.write('---')
st.subheader('Data Description table')
st.write(''' This table describes the statistical property of the above dataset.''')
st.dataframe(df.describe().transpose())

df_details_tbl = pd.DataFrame({
    'Unique':df.nunique(),
    'data_type':df.dtypes.values,
    'Null':df.isna().sum(), 
    'null_percent':df.isna().sum()/len(df)
})

st.write('---')
st.subheader('Dataset Details table')
st.write('''
    This table describes the data types, null values and unique values of the columns.
''')
st.table(df_details_tbl)

numerical_dtypes = df.select_dtypes(exclude='O')
categorical_dtypes = df.select_dtypes(include='O')

st.write('---')
st.subheader('Numerical Data Types in the dataframe')
st.dataframe(numerical_dtypes.head(5))

st.write('---')
st.subheader('Categorical Data Types in the dataframe')
st.dataframe(categorical_dtypes.head(5))

"""# **Visualizations** 📈

"""

sns.set_style('darkgrid')
colors = ['#ED72A3','#8565F0','#22559C', '#F27370','#FA9856','#EDE862']

# heatmaps
# '''
#     The correlation is only possible to numerical values.
# '''

st.subheader('Heatmap of the correlation of the numerical values')
fig= plt.figure()
sns.heatmap(df.corr(), annot=True, fmt='.1f')
st.pyplot(fig)


# visualizations on the mean of open, high, low, close and volume with year, month and day.

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month

st.write('---')
st.subheader('__Barplot of__ _"Volume with respect to the year"_')
fig, ax = plt.subplots()
sns.barplot(data=df, x='Year', y='Volume')
st.write(fig)

st.write('---')
st.subheader('__Lineplot of__ _"Volume with respect to the year"_')
fig, ax= plt.subplots()
sns.lineplot(data=df, x='Year', y='Volume', palette=colors, errorbar=None)
st.write(fig)

st.write('---')
st.subheader('__Lineplot of__ _"Close with respect to the year"_')
fig, ax=plt.subplots()
sns.lineplot(data=df, x='Year', y='Close', errorbar=None)
st.write(fig)




# fig=plt.figure(figsize=(15,7))
# plt.plot(df['Date'], df['Volume'])
# st.pyplot(fig)
st.write('---')
st.subheader('__Linechart__ of _Close_')
st.line_chart(df['Close'])

st.write('---')
st.subheader('__Linechart__ of _Volume_')
st.line_chart(df['Volume'])

