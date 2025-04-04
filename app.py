import streamlit as st
import requests

API_URL = "http://localhost:8000/recommend"

st.title("SHL Assessment Recommender")

query = st.text_area("Enter job description or search query:")

if st.button("Recommend Assessments"):
    response = requests.post(API_URL, json={"text": query})
    recommendations = response.json()

    for rec in recommendations:
        st.write(f"### [{rec['name']}]({rec['url']})")
        st.write(f"- **Duration**: {rec['duration']} mins")
        st.write(f"- **Remote Testing**: {rec['remote']}")
        st.write(f"- **Adaptive/IRT**: {rec['adaptive']}")
        st.write("---")
