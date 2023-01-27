'''
    EDA performed by aakash shakya
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st

df = pd.read_csv('nepsealpha_export_price_NABIL_2013-01-26_2023-01-26.csv')

st.write('DataFrame head(10)')
st.write(df.head(10))

st.write(f'Data Shape = {df.shape}')


st.write('Data Description')
st.write(df.describe().transpose())

df_details_tbl = pd.DataFrame({
    'Unique':df.nunique(),
    'data_type':df.dtypes.values,
    'Null':df.isna().sum(), 
    'null_percent':df.isna().sum()/len(df)
})

st.write('Data Details table')
df_details_tbl

numerical_dtypes = df.select_dtypes(exclude='O')
categorical_dtypes = df.select_dtypes(include='O')

st.write('Numerical Data Types in the dataframe')
st.write(numerical_dtypes.head(5))

st.write('Categorical Data Types in the dataframe')
st.write(categorical_dtypes.head(5))

"""# **Visualizations**

"""

sns.set_style('darkgrid')
colors = ['#ED72A3','#8565F0','#22559C', '#F27370','#FA9856','#EDE862']

# heatmaps
'''
    The correlation is only possible to numerical values.
'''
fig= plt.figure()
sns.heatmap(df.corr(), annot=True, fmt='.1f')
st.pyplot(fig)


# visualizations on the mean of open, high, low, close and volume with year, month and day.

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month

fig, ax = plt.subplots()
sns.barplot(data=df, x='Year', y='Volume')
st.write(fig)

fig, ax= plt.subplots()
sns.lineplot(data=df, x='Year', y='Volume', palette=colors, ci=None)
st.write(fig)

fig, ax=plt.subplots()
sns.lineplot(data=df, x='Year', y='Close', ci=None)
st.write(fig)

# end_year, e = st.select_slider('select a year', options=df['Year'].unique()) 
# print(end_year, e)
# print(df[df['Year']<end_year])


fig=plt.figure(figsize=(15,7))
plt.plot(df['Date'], df['Volume'])
st.pyplot(fig)


