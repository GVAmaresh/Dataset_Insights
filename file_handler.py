import streamlit as st
import pandas as pd
import visualizations

def data_exploration_page():
    uploaded_file = st.sidebar.file_uploader("📁 Upload your dataset (CSV format)", type="csv")
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state.df = df
            st.sidebar.success("File uploaded successfully!")

            st.expander("🔍 Uploaded Dataset Preview", expanded=True)
            st.dataframe(df.head())
            st.markdown(f"**Rows:** {df.shape[0]}, **Columns:** {df.shape[1]}")
            st.markdown("---")
            st.markdown("### Full Dataset Summary")
            st.write(df.describe())
            visualizations.data_visualization(df)
        except Exception as e:
            st.error("🚨 Error reading the uploaded file. Please ensure it is a valid CSV file.")
