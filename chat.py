import streamlit as st
from pandasai import SmartDataframe
from pandasai.llm.google_gemini import GoogleGemini

llm = GoogleGemini(api_key='AIzaSyDvVLs3rkuynWcImZdstH6I-ecsqzEyHjs')

def chat_page():
    if st.session_state.df is None:
        st.error("Please upload and explore a dataset before using this feature!")
        st.stop()

    df = st.session_state.df
    updated_df = SmartDataframe(df, config={"llm": llm})

    suggested_prompts = [
        "What is the average value of column X?",
        "Show me the distribution of column Y.",
        "Filter rows where column Z is greater than A.",
        "What insights can you provide about this dataset?",
    ]

    with st.form("chat_form"):
        chat_prompt = st.text_area("Type your prompt here...", placeholder="e.g., What are the trends in this dataset?")
        selected_prompt = st.radio("Choose a suggested prompt:", options=["None"] + suggested_prompts)
        if selected_prompt != "None":
            chat_prompt = selected_prompt

        submitted = st.form_submit_button("Submit")
        if submitted:
            if not chat_prompt.strip():
                st.error("Please enter a prompt before submitting!")
            else:
                try:
                    response = updated_df.chat(chat_prompt)
                    st.markdown("### Response:")
                    st.text_area("Response:", value=response, height=200)
                except Exception as e:
                    st.error(f"An error occurred while processing your prompt: {e}")
