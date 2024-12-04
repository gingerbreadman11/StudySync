# app.py

# test

# test von Scott

# hier bin ich

import streamlit as st
from gui_input import get_user_inputs
from calculations import generate_study_plan
from output_display import display_schedule

def main():
    inputs = get_user_inputs()

    if st.session_state.get('plan_generated', False):
        # Generate the study plan
        schedule = generate_study_plan(inputs)
        display_schedule(schedule)
    else:
        st.write("Please enter your inputs and click 'Generate Study Plan'.")

if __name__ == '__main__':
    main()
