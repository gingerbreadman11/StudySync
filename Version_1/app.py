#to run use streamlit run app.py and open it upo in the browser
from gui_input import get_user_inputs
from calculations import generate_study_plan
from output_display import display_study_plan

def main():
    user_inputs = get_user_inputs()
    if user_inputs:
        study_plan = generate_study_plan(user_inputs)
        display_study_plan(study_plan)

if __name__ == "__main__":
    main()
