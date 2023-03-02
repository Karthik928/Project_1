import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os



st.title("Dashboard - Titanic Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

df=pd.read_csv(DATA_PATH)
st.dataframe(df)

who = st.selectbox("Select who:", df['who'].unique())

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89']
df['Age'] = pd.cut(df['age'], bins=bins, labels=labels, include_lowest=True)
df = df.sort_values('Age')

st.subheader("Number of Passengers Survived based on age")

fig_1 = px.histogram(df[df['who'] == who], x="Age", nbins=10, color="survived")
st.plotly_chart(fig_1, use_container_width=True)

df = df.sort_values('pclass')

fig_2 = px.pie(df[df['who'] == who], names="pclass", title="Passenger Class Distribution")
st.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.box(df, y='Age', title='Age Distribution by Survival Status', color="survived")
st.plotly_chart(fig_3, use_container_width=True)
