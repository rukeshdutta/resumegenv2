import streamlit as st
from config import SECTIONS

def render_ui():
    st.title("Job Description to Resume Section Generator")

    job_description = st.text_area("Enter the job description", height=200)
    
    col1, col2 = st.columns(2)
    with col1:
        selected_section = st.selectbox("Select section to generate", SECTIONS)
    with col2:
        max_words = st.number_input("Maximum words for the section", min_value=50, max_value=500, value=200, step=50)
    
    return job_description, selected_section, max_words