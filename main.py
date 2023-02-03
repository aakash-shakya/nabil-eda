'''
    EDA performed by aakash shakya
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle as pkl

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

    st.markdown(f'''<span style="color:black">●</span> [___DataFrame___](#dataframe)''', unsafe_allow_html=True)
    
    st.markdown(f'''<span style="color:black">●</span> [___Visualizations___](#visualizations)''', unsafe_allow_html=True)

    st.markdown(f'''<span style="color:black">●</span> [___Linear regression model___](#linear-regression-model)''', unsafe_allow_html=True)

    st.markdown('''
    ---
    Created with ❤️ by [aakas](https://aakas.com.np).
    ''')

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
sns.heatmap(numerical_dtypes.corr(), annot=True, fmt='.1f')
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
sns.lineplot(data=df, x='Year', y='Volume', errorbar=None)
st.write(fig)

st.write('---')
st.subheader('__Lineplot of__ _"Close with respect to the year"_')
fig, ax=plt.subplots()
sns.lineplot(data=df, x='Year', y='Close', errorbar=None)
st.write(fig)


st.write('---')
st.subheader('__Linechart__ of _Close_')
st.line_chart(data=df, x='Date', y='Close')

st.write('---')
st.subheader('__Linechart__ of _Volume_')
st.line_chart(data=df, x='Date', y='Volume')


################################## Linear Regression Model ########################################

st.subheader('Linear Regression Model')
st.write('''
---
    In this section we will be using the linear regression model to predict the closing price of the stock.
    To predict the closing price of the stock we will be using the following features:
    1. Open
    2. High
    3. Low
''')


model = pkl.load(open('model.pkl', 'rb'))

st.write('Enter the values for the following features to predict the closing price of the stock.')

col1, col2, col3 = st.columns(3)

with col1:
    open = st.number_input('Open', min_value=0.0, max_value=100000.0, value=0.0, on_change=None)
with col2:
    high = st.number_input('High', min_value=0.0, max_value=100000.0, value=0.0, on_change=None)
with col3:
    low = st.number_input('Low', min_value=0.0, max_value=100000.0, value=0.0, on_change=None)
    

if st.button('Predict'):
    volume = model.predict([[open, high, low]])
    st.markdown("""
    <style>
    .result{
        font-size: 20px;
        color: black;
        background-color: #6096B4;
    }
    </style> """ + f"""
    <p class='result'>The predicted closing price of the stock is:    {volume[0][0]}</p>""", unsafe_allow_html=True)