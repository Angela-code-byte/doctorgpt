# app.py

import streamlit as st
from utils.ocr_utils import extract_text_from_pdf

st.set_page_config(page_title="DoctorGPT - Blood Report Reader")

st.title("🧬 DoctorGPT: Smart Blood Report Analyzer")

uploaded_file = st.file_uploader("📄 Upload your blood report (PDF only)", type=["pdf"])

if uploaded_file is not None:
    st.success("✅ File uploaded successfully.")
    with st.spinner("🔍 Extracting text..."):
        extracted_text = extract_text_from_pdf(uploaded_file)
    st.subheader("📝 Extracted Text")
    st.text_area("Result", extracted_text, height=300)
from utils.llm_utils import summarize_medical_text

if st.button("🧠 Explain Report with AI"):
    with st.spinner("🔬 Analyzing with LLM..."):
        explanation = summarize_medical_text(extracted_text)
    st.subheader("📘 DoctorGPT Explanation")
    st.write(explanation)
from utils.food_utils import get_nutrition_advice, plot_nutrient_chart

if st.button("🥗 Get Nutrition Suggestions"):
    with st.spinner("🧾 Checking for nutrient markers..."):
        tips = get_nutrition_advice(extracted_text)

    if tips:
        st.subheader("🥦 Personalized Food Suggestions")

        for item in tips:
            st.markdown(f"**🩺 {item['deficiency']}**")
            st.markdown(f"👉 Eat more: _{', '.join(item['recommend'])}_")
        
        # Plot chart
        chart = plot_nutrient_chart(tips)
        st.plotly_chart(chart, use_container_width=True)
    else:
        st.info("No nutrition-related terms found in the report.")
