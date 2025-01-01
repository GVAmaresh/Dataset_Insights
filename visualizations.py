import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def data_visualization(df):
    if st.sidebar.checkbox("Show Data Visualization"):
        column_to_plot = st.sidebar.selectbox("Select Column for Visualization", df.columns)
        plot_type = st.sidebar.selectbox("Select Plot Type", ["Bar", "Line", "Histogram"])

        plt.figure(figsize=(10, 5))
        if plot_type == "Bar":
            sns.countplot(data=df, x=column_to_plot)
        elif plot_type == "Line":
            df[column_to_plot].value_counts().sort_index().plot(kind='line')
        elif plot_type == "Histogram":
            plt.hist(df[column_to_plot], bins=20)

        plt.title(f"{plot_type} of {column_to_plot}")
        plt.xlabel(column_to_plot)
        plt.ylabel("Count")
        st.pyplot(plt)
