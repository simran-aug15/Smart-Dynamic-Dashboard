import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page setup
st.set_page_config(layout="wide")
st.title("Smart Dashboard Data Analytics")

# Upload file
file = st.file_uploader("Upload CSV file")

if file:
    df = pd.read_csv(file)

    # Data preview
    st.subheader("📁 Data Preview")
    st.dataframe(df)

    # Detect numeric columns
    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    # Sidebar controls
    st.sidebar.title("🎮 Controls")

    chart_type = st.sidebar.selectbox(
        "Select Chart Type",
        ["Bar Chart", "Line Chart", "Pie Chart", "Histogram","KDE Plot","Scatter Plot","Box Plot","Pair Plot"]
    )

    # Select X-axis
    x_col = st.sidebar.selectbox("Select X-axis", df.columns)

    if numeric_cols:

        # Select Y-axis
        y_col = st.sidebar.selectbox("Select Y-axis", numeric_cols)

        st.subheader("📊 Visualization")

        # Bar Chart
        if chart_type == "Bar Chart":
            st.bar_chart(df[[x_col, y_col]].set_index(x_col))

        # Line Chart
        elif chart_type == "Line Chart":
            st.line_chart(df[[x_col, y_col]].set_index(x_col))

        # Pie Chart
        elif chart_type == "Pie Chart":
            pie_data = df.groupby(x_col)[y_col].sum()

            fig, ax = plt.subplots(figsize=(3,3))
            ax.pie(
                pie_data,
                labels=pie_data.index,
                autopct="%1.1f%%",
                startangle=90,
                pctdistance=0.8
            )

            ax.set_title(f"{y_col} by {x_col}")
            st.pyplot(fig)

        #Histogram
        elif chart_type=="Histogram":
              fig, ax = plt.subplots(figsize=(7,5))
              sns.histplot(df[y_col], bins=20, kde=False)
              plt.set_title(f"Histogram of {y_col}")
              st.pyplot(fig)
              
        #KDE plot
        elif chart_type=="KDE Plot":
            fig,ax=plt.subplots(figsize=(3,3))
            sns.kdeplot(data=df[y_col],)
            sns.kdeplot(df[y_col], fill=True)
            plt.set_title(f"KDE Plot of {y_col}")
            st.pyplot(fig)








        # Statistics
        st.subheader("📈 Statistics")
        st.write(df[y_col].describe())

    else:
        st.warning("No numeric columns found in the uploaded data.")