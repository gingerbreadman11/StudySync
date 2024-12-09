import streamlit as st
from gui_input import get_user_inputs
from calculations import generate_study_plan
from output_display import display_schedule
from datetime import datetime, timedelta, time

def main():

    events = {'training': [time(16,00), 2.0], 'dinner': [time(19,00), 1.0]}
    exams = {'Calculus': datetime(2025, 1, 7, 10, 0), 
            'Electronic Circuits': datetime(2025, 2, 4, 9, 30),
            'Linear Algebra': datetime(2025, 1, 13, 11, 0)
            }
    inputs = events, exams

    schedule = generate_study_plan(inputs)
    display_schedule(schedule)

if __name__ == '__main__':
    main()
