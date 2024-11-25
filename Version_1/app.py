

import streamlit as st
from gui_input import get_user_inputs
from calculations import generate_study_plan
from output_display import display_study_plan

def main():
    exams = get_user_inputs()
    if exams:
        study_plans, study_schedule = generate_study_plan(exams)
        display_study_plan(study_plans, study_schedule)

if __name__ == "__main__":
    main()
