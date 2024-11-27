# calculations.py

from datetime import datetime, date, time, timedelta

def generate_study_plan(inputs):
    type1_start_time = inputs['type1_start_time']
    type1_duration = inputs['type1_duration']
    exam_date = inputs['exam_date']

    today = date.today()
    days_until_exam = (exam_date - today).days

    if days_until_exam < 0:
        return None, "Error: Exam date must be in the future."

    # Initialize the schedule dictionary
    schedule = {}

    for day in range(days_until_exam + 1):
        current_date = today + timedelta(days=day)
        schedule[current_date] = []

        # Schedule Type 1 activity
        type1_end_datetime = datetime.combine(current_date, type1_start_time) + timedelta(hours=type1_duration)
        type1_end_time = type1_end_datetime.time()

        schedule[current_date].append({
            'activity': 'Type 1',
            'start_time': type1_start_time,
            'end_time': type1_end_time
        })

        # Schedule Type 2 activity (Studying) around Type 1
        # Assume study hours are from 8 AM to 10 PM
        day_start = time(8, 0)
        day_end = time(22, 0)

        # Available slots before and after Type 1 activity
        if type1_start_time > day_start:
            schedule[current_date].append({
                'activity': 'Study',
                'start_time': day_start,
                'end_time': type1_start_time
            })

        if type1_end_time < day_end:
            schedule[current_date].append({
                'activity': 'Study',
                'start_time': type1_end_time,
                'end_time': day_end
            })

    return schedule, None
