#this code does not work with the newest python 3.13
import PySimpleGUI as sg
import datetime
from datetime import timedelta
def main():
    sg.theme('LightBlue')  # You can choose a different theme if you like

    exams = []

    # Define the window layout
    layout = [
        [sg.Text('Exam Name', size=(20, 1)), sg.InputText(key='name')],
        [sg.Text('Exam Date (YYYY-MM-DD)', size=(20, 1)), sg.InputText(key='date'), sg.CalendarButton('Choose Date', target='date', format='%Y-%m-%d')],
        [sg.Text('Difficulty Level', size=(20, 1)), sg.Combo(['Easy', 'Medium', 'Hard'], default_value='Medium', key='difficulty')],
        [sg.Text('Preparation Time (days)', size=(20, 1)), sg.InputText(key='prep_time')],
        [sg.Button('Add Exam'), sg.Button('Generate Study Plan'), sg.Button('Clear Exams'), sg.Button('Exit')],
        [sg.HorizontalSeparator()],
        [sg.Text('Study Plan Output')],
        [sg.Multiline(size=(60, 15), key='output', disabled=True)]
    ]

    window = sg.Window('Study Planner', layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break

        elif event == 'Add Exam':
            # Validate and add exam
            name = values['name'].strip()
            date_str = values['date'].strip()
            difficulty = values['difficulty']
            prep_time_str = values['prep_time'].strip()

            if not name:
                sg.popup_error("Exam name cannot be empty.")
                continue

            # Validate date
            try:
                exam_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                if exam_date < datetime.date.today():
                    sg.popup_error("Exam date cannot be in the past.")
                    continue
            except ValueError:
                sg.popup_error("Please enter the date in YYYY-MM-DD format or select from the calendar.")
                continue

            # Validate preparation time
            try:
                prep_time = int(prep_time_str)
                if prep_time <= 0:
                    sg.popup_error("Preparation time must be a positive integer.")
                    continue
            except ValueError:
                sg.popup_error("Preparation time must be a number.")
                continue

            exam = {
                'name': name,
                'date': exam_date,
                'difficulty': difficulty,
                'prep_time': prep_time
            }
            exams.append(exam)

            # Clear input fields
            window['name'].update('')
            window['date'].update('')
            window['prep_time'].update('')

            sg.popup_ok(f"Exam '{name}' added successfully.")

        elif event == 'Generate Study Plan':
            if not exams:
                sg.popup_error("No exams added. Please add at least one exam.")
                continue
            study_plan = generate_study_plan(exams)
            display_study_plan(study_plan, window)

        elif event == 'Clear Exams':
            exams.clear()
            window['output'].update('')
            sg.popup_ok("All exams have been cleared.")

    window.close()

def generate_study_plan(exams):
    study_plan = []
    for exam in exams:
        sessions = []
        today = datetime.date.today()
        start_date = exam['date'] - timedelta(days=exam['prep_time'])
        if start_date < today:
            start_date = today

        total_days = (exam['date'] - start_date).days
        # Simple algorithm: Study every day from start_date to the day before the exam
        for i in range(total_days):
            study_day = start_date + timedelta(days=i)
            sessions.append(study_day)

        study_plan.append({
            'exam_name': exam['name'],
            'study_sessions': sessions
        })
    return study_plan

def display_study_plan(study_plan, window):
    output = "Your Study Plan:\n"
    for plan in study_plan:
        output += f"\nExam: {plan['exam_name']}\n"
        output += "Study Sessions:\n"
        for session in plan['study_sessions']:
            output += f" - {session.strftime('%Y-%m-%d')}\n"
    window['output'].update(output)

if __name__ == "__main__":
    main()
