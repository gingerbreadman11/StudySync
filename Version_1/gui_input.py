import streamlit as st
from datetime import datetime

def get_user_inputs():
    st.title("📚 StudySync - Exam and Study Planning")

    st.header("Enter Exam Details")

    exam_date = st.date_input("Exam Date")
    difficulty_level = st.selectbox("Difficulty Level", ["Easy", "Medium", "Hard"])
    prep_time = st.number_input("Desired Preparation Time (hours)", min_value=1, value=10)
    personal_preferences = st.text_area("Personal Preferences (e.g., preferred study times)")

    submit = st.button("Generate Study Plan")

    if submit:
        inputs = {
            "exam_date": exam_date,
            "difficulty_level": difficulty_level,
            "prep_time": prep_time,
            "personal_preferences": personal_preferences
        }
        return inputs
    else:
        return None
