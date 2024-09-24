import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data(1990)')
df = pd.read_csv('Housing.csv')

# note that you have to use 0 and 500001 given that the data type of price is float
price_filter = st.slider('Minimal Median House Price:', 0, 500001, 200000)  # min, max, default

# create a multi select
location_filter = st.sidebar.multiselect(
     'choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults
# 创建单选按钮选择收入水平
median_income = st.sidebar.radio(
    "Select Income Level：",
    options=['Low ', 'Medium', 'High']
)



# filter by price
df = df[df.median_house_value >= price_filter]

# filter by capital
df = df[df.ocean_proximity.isin(location_filter)]

# 使用 if 语句过滤 DataFrame
if median_income == 'Low':
    filtered_df = df[df['median_income'] <= 2.5]
elif median_income == 'Medium ':
    filtered_df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:  # 'high'
    filtered_df = df[df['median_income'] > 4.5]

# show on map
st.map(df)



# show the plot
st.markdown("Median House Value vs Freqrency")
plt.figure(figsize=(10, 5))
plt.hist(df['median_house_value'], bins=30, color='blue', alpha=0.5)
plt.xlabel("Median House Value")
plt.ylabel("Frequency")
plt.title("Median House Value vs Freqrency")
plt.xlim(df['median_house_value'].min(), df['median_house_value'].max())
plt.grid(axis='y', alpha=0.5)


st.pyplot(plt)