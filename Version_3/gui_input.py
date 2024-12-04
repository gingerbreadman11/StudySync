import streamlit as st
from datetime import datetime, time, date, timedelta

def get_user_inputs():
    st.title("📅 Study Plan Generator")

    # Initialize session state for events and exams
    if "events" not in st.session_state:
        st.session_state["events"] = {}

    if "exams" not in st.session_state:
        st.session_state["exams"] = {}

    # Non-Negotiable Events Section
    st.header("Non-Negotiable Events")
    event_name = st.text_input("Event Name", key="event_name")
    event_start_time = st.time_input("Event Start Time", key="event_start_time")
    event_duration = st.number_input(
        "Event Duration (hours)", min_value=0.5, max_value=24.0, step=0.5, key="event_duration"
    )
    add_event = st.button("Add Event")

    if add_event and event_name:
        st.session_state["events"][event_name] = [event_start_time, event_duration]
        st.success(f"Added event: {event_name}")

    if not st.session_state["events"]:
        st.write("No non-negotiable events added yet.")

    # Exams Section
    st.header("Exams")
    exam_name = st.text_input("Exam Name", key="exam_name")
    exam_date = st.date_input("Exam Date", min_value=date.today(), key="exam_date")
    exam_time = st.time_input("Exam Time", key="exam_time")  # Add time input
    add_exam = st.button("Add Exam")

    if add_exam and exam_name:
        # Combine exam_date and exam_time into a datetime object
        exam_datetime = datetime.combine(exam_date, exam_time)
        st.session_state["exams"][exam_name] = exam_datetime
        st.success(f"Added exam: {exam_name}")

    if not st.session_state["exams"]:
        st.write("No exams added yet.")

    # Generate study plan button
    generate_plan = st.button("Generate Study Plan")

    # Return inputs if generate_plan is clicked
    if generate_plan:
        # Prepare the final output
        events = st.session_state["events"]
        exams = st.session_state["exams"]
        output = events, exams
        st.session_state['plan_generated'] = True  # Set the plan_generated flag
        st.success("Study plan inputs saved successfully!")
        return output

    # Default return when 'Generate Study Plan' is not clicked
    return st.session_state.get("events", {}), st.session_state.get("exams", {})
