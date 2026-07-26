import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Page setup
st.set_page_config(layout="wide")
set.title("Smart Dashboard Data Analytics")

#Upload file
file =st.file_uploder("Upload CSV file")
if file:
    df=pd.read_csv(file)

#Data preview
st.subheader("📁Data Preview")  
st.dataframe(df)  

#Detect columns
numeric_cols=df.select_dtypes(include='number').columns.tolist()

#Sidebar controls
st.sidebar("🎮 Controls")

chart_type=st.sidebar.selectbox("Select Chart Type",["Bar Chart","Line Chart","Pie Chart"])

#Select columns
x_col=st.sidebar.selectbox("Select X-axis",df.columns)

if numeric_cols:
    y_col=st.sidebar.selectbox("Select Y-axis",numeric_cols)