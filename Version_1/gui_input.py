# gui_input.py

import streamlit as st
from datetime import datetime, time

def get_user_inputs():
    st.title("📚 StudySync - Exam and Study Planning")

    st.header("Daily Schedule Preferences")

    # Sleep settings
    st.subheader("Sleep Settings")

    sleep_start_time = st.time_input("Sleep Start Time", value=time(22, 0))
    sleep_duration = st.number_input("Sleep Duration (hours)", min_value=0.0, max_value=24.0, value=8.0, step=0.5)

    # Eating times
    st.subheader("Eating Times")

    # Initialize session state for eating times
    if "eating_times" not in st.session_state:
        st.session_state.eating_times = []

    # Function to add a new eating time
    def add_eating_time():
        st.session_state.eating_times.append({
            "start_time": time(12, 0),
            "duration": 1.0
        })

    # Button to add a new eating time
    if st.button("Add Eating Time"):
        add_eating_time()

    # Display input fields for each eating time
    for idx, eating_time in enumerate(st.session_state.eating_times):
        st.markdown(f"**Eating Time {idx + 1}**")

        col1, col2 = st.columns(2)
        with col1:
            start_time = st.time_input(
                f"Eating Start Time {idx + 1}",
                value=eating_time["start_time"],
                key=f"eating_start_time_{idx}"
            )
        with col2:
            duration = st.number_input(
                f"Eating Duration (hours) {idx + 1}",
                min_value=0.0,
                max_value=24.0,
                value=eating_time["duration"],
                step=0.25,
                key=f"eating_duration_{idx}"
            )

        # Update the eating time data in session state
        st.session_state.eating_times[idx] = {
            "start_time": start_time,
            "duration": duration
        }

        # Option to remove an eating time
        if st.button(f"Remove Eating Time {idx + 1}"):
            st.session_state.eating_times.pop(idx)
            st.experimental_rerun()

    # Workout times
    st.subheader("Workout Times")

    # Initialize session state for workout times
    if "workout_times" not in st.session_state:
        st.session_state.workout_times = []

    # Function to add a new workout time
    def add_workout_time():
        st.session_state.workout_times.append({
            "start_time": time(17, 0),
            "duration": 1.0
        })

    # Button to add a new workout time
    if st.button("Add Workout Time"):
        add_workout_time()

    # Display input fields for each workout time
    for idx, workout_time in enumerate(st.session_state.workout_times):
        st.markdown(f"**Workout Time {idx + 1}**")

        col1, col2 = st.columns(2)
        with col1:
            start_time = st.time_input(
                f"Workout Start Time {idx + 1}",
                value=workout_time["start_time"],
                key=f"workout_start_time_{idx}"
            )
        with col2:
            duration = st.number_input(
                f"Workout Duration (hours) {idx + 1}",
                min_value=0.0,
                max_value=24.0,
                value=workout_time["duration"],
                step=0.25,
                key=f"workout_duration_{idx}"
            )

        # Update the workout time data in session state
        st.session_state.workout_times[idx] = {
            "start_time": start_time,
            "duration": duration
        }

        # Option to remove a workout time
        if st.button(f"Remove Workout Time {idx + 1}"):
            st.session_state.workout_times.pop(idx)
            st.experimental_rerun()

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
            "prep_time": 10.0,
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
                min_value=1.0,
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
        inputs = {
            "sleep_start_time": sleep_start_time,
            "sleep_duration": sleep_duration,
            "eating_times": st.session_state.eating_times,
            "workout_times": st.session_state.workout_times,
            "exams": st.session_state.exams
        }
        return inputs
    else:
        return None
