
# gui_input.py

import streamlit as st
from datetime import datetime, time, date

def get_user_inputs():
    st.title("📅 Study Plan Generator")

    st.header("Non-Negotiable Activity")

    # Get Type 1 activity start time and duration
    type1_start_time = st.time_input(
        "Type 1 Activity Start Time", value=st.session_state.get('type1_start_time', time(9, 00))
    )
    type1_duration = st.number_input(
        "Type 1 Activity Duration (hours)",
        min_value=0.5,
        max_value=24.0,
        value=st.session_state.get('type1_duration', 1.0),
        step=0.5
        
    )

    st.header("Exam Details (Type 2)")

    # Get exam date
    exam_date = st.date_input(
        "Exam Date", min_value=date.today(), value=st.session_state.get('exam_date', date.today())
    )

    # Generate study plan button
    generate_plan = st.button("Generate Study Plan")

    # Return inputs if generate_plan is clicked
    if generate_plan:
        inputs = {
            'type1_start_time': type1_start_time,
            'type1_duration': type1_duration,
            'exam_date': exam_date
        }
        # Store inputs in session state
        st.session_state['inputs'] = inputs
        st.session_state['plan_generated'] = True
    else:
        # If inputs are already in session state, retrieve them
        inputs = st.session_state.get('inputs', None)

    return inputs