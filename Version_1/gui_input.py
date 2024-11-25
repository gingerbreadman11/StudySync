# gui_input.py

import streamlit as st
from datetime import datetime

def get_user_inputs():
    st.title("📚 StudySync - Exam and Study Planning")

    st.header("Enter Exam Details")

    # Initialize session state for exams
    if "exams" not in st.session_state:
        st.session_state.exams = []

    # Function to add a new exam
    def add_exam():
        st.session_state.exams.append({
            "exam_name": f"Exam {len(st.session_state.exams) + 1}",
            "exam_date": datetime.today().date(),
            "difficulty_level": "Medium",
            "prep_time": 10,
            "personal_preferences": ""
        })

    # Button to add a new exam
    if st.button("Add Exam"):
        add_exam()

    # Display input fields for each exam
    for idx, exam in enumerate(st.session_state.exams):
        st.subheader(f"Exam {idx + 1}")

        # Exam Name Input Field
        exam_name = st.text_input(
            f"Exam Name {idx + 1}",
            value=exam["exam_name"],
            key=f"exam_name_{idx}"
        )

        col1, col2 = st.columns(2)

        with col1:
            exam_date = st.date_input(
                f"Exam Date {idx + 1}",
                value=exam["exam_date"],
                key=f"exam_date_{idx}"
            )
            prep_time = st.number_input(
                f"Desired Preparation Time (hours) {idx + 1}",
                min_value=1,
                value=exam["prep_time"],
                key=f"prep_time_{idx}"
            )
        with col2:
            difficulty_level = st.selectbox(
                f"Difficulty Level {idx + 1}",
                ["Easy", "Medium", "Hard"],
                index=["Easy", "Medium", "Hard"].index(exam["difficulty_level"]),
                key=f"difficulty_level_{idx}"
            )
            personal_preferences = st.text_area(
                f"Personal Preferences {idx + 1} (e.g., preferred study times)",
                value=exam["personal_preferences"],
                key=f"personal_preferences_{idx}"
            )

        # Update the exam data in session state
        st.session_state.exams[idx] = {
            "exam_name": exam_name,
            "exam_date": exam_date,
            "difficulty_level": difficulty_level,
            "prep_time": prep_time,
            "personal_preferences": personal_preferences
        }

        # Option to remove an exam
        if st.button(f"Remove Exam {idx + 1}"):
            st.session_state.exams.pop(idx)
            st.experimental_rerun()

    if st.session_state.exams:
        submit = st.button("Generate Study Plan")
    else:
        st.info("Please add at least one exam.")
        submit = False

    if submit:
        return st.session_state.exams
    else:
        return None
