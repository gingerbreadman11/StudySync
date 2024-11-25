# app.py

# import streamlit as st
# from gui_input import get_user_inputs
# from calculations import generate_study_plan
# from output_display import display_study_plan

# def main():
#     inputs = get_user_inputs()
#     if inputs:
#         study_plans, study_schedule = generate_study_plan(inputs)
#         display_study_plan(study_plans, study_schedule)

# if __name__ == "__main__":
#     main()
# app.py

import streamlit as st
from output_display import display_study_plan
from datetime import datetime, date, time, timedelta

def main():
    # Sample study plan data
    study_plans = []

    # Today's date
    today = date.today()

    # Sample study schedule
    study_schedule = {
        today: [
            {
                'activity': 'Study',
                'exam_name': 'Mathematics',
                'start_time': '10:00',
                'end_time': '12:00'
            },
            {
                'activity': 'Study',
                'exam_name': 'Physics',
                'start_time': '14:00',
                'end_time': '16:00'
            }
        ],
        today + timedelta(days=1): [
            {
                'activity': 'Study',
                'exam_name': 'Chemistry',
                'start_time': '09:00',
                'end_time': '11:00'
            }
        ]
    }

    display_study_plan(study_plans, study_schedule)

if __name__ == "__main__":
    main()
