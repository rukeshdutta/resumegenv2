import streamlit as st
from ui import render_ui
from resume_generator import generate_resume_section, optimize_for_ats
from keyword_extractor import extract_keywords

def main():
    st.set_page_config(page_title="Job Description to Resume Section Generator", layout="wide")
    
    job_description, selected_section, max_words = render_ui()
    
    if st.button("Generate Section"):
        if job_description and selected_section:
            # Extract keywords from job description
            extracted_keywords = extract_keywords(job_description)
            
            # Display extracted keywords and allow user to edit
            st.subheader("Extracted Keywords")
            keywords = st.text_area("Edit or add more keywords (comma-separated)", ", ".join(extracted_keywords))
            keyword_list = [k.strip() for k in keywords.split(',')]
            
            # Generate initial resume section
            generated_section = generate_resume_section(job_description, keyword_list, selected_section, max_words)
            
            st.subheader(f"Generated {selected_section} Section")
            st.text_area("Generated Content", generated_section, height=200)
            
            # Store the generated section in session state
            st.session_state.generated_section = generated_section
            st.session_state.job_description = job_description
            st.session_state.keyword_list = keyword_list
            
            # Show the "Optimize for ATS" button
            st.button("Optimize for ATS", key="optimize_button")
        else:
            st.warning("Please enter the job description and select a section.")
    
    # Check if the "Optimize for ATS" button was clicked
    if "optimize_button" in st.session_state and st.session_state.optimize_button:
        if hasattr(st.session_state, 'generated_section'):
            optimized_section = optimize_for_ats(
                st.session_state.generated_section,
                st.session_state.job_description,
                st.session_state.keyword_list
            )
            st.subheader(f"ATS-Optimized {selected_section} Section")
            st.text_area("Optimized Content", optimized_section, height=200)
        else:
            st.warning("Please generate a section first before optimizing for ATS.")

if __name__ == "__main__":
    main()
