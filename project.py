import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Page setup
st.set_page_config(layout="wide")
st.title("Smart Dashboard Data Analytics")

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

    st.subheader(" 📊 Visualization")   


    # Bar Chart
    if chart_type=="Bar Chart":
        st.bar_chart(df[[x_col,y_col]].set_index(x_col))  #As in dataframe we automatically get the index values of the data and take it as the x-axis but we donot need it as x-axis so we make index as x selected value by user 


    #Line Chart
    elif chart_type=="Line Chart":
        st.line_chart(df[[x_col,y_col]].set_index(x_col))

    #Pie chart
    elif chart_type=="Pie Chart":
        pie_data=df.groupby(x_col)[y_col].sum()

        fig,ax=plt.subplots(figsize=(5,5))
        ax.pie(
            pie_data,
            labels=pie_data.index,
            autopct="%1.1f%%",
            startangle=90,
            pctdistance=0.8

        )       

    #Statistics
    st.sunheader("📈 Statistics")    
    st.write(df[y_col].describe())


else:
    st.warning("No numeric columns found in data ")
