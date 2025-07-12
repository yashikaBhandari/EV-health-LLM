import streamlit as st
import pandas as pd
from generate_report import generate_ev_report

st.set_page_config(page_title="EV Health Report Generator", page_icon="🔋")

st.title("🔋 EV Health Report Generator using LLM")
st.markdown("Upload EV sensor data and get instant health summaries using GPT.")

uploaded_file = st.file_uploader("📤 Upload your EV CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Raw Data")
    st.dataframe(df)

    st.subheader("📄 LLM-Generated Health Reports")

    for idx, row in df.iterrows():
        with st.expander(f"🚗 Report for {row['vehicle_id']}"):
            summary = generate_ev_report(row)
            st.write(summary)
