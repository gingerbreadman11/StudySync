from datetime import datetime, timedelta, time

def generate_study_plan(inputs):
    events, exams = inputs
    
    schedule = {}
    

    # exams sorted by dates
    sorted_exams = sorted(exams.items(), key=lambda x: x[1])  # Sort by exam date
    exam_cycle = [exam for exam, _ in sorted_exams]  # Maintain the cycle order
    num_exams = len(exam_cycle)
    
    # Add all exams to schedule
    for exam_name, exam_start in exams.items():

        exam_end = (exam_start + timedelta(hours=2)).time()

        day_of_exam = exam_start.date()
        if day_of_exam not in schedule:
            schedule[day_of_exam] = []
        schedule[day_of_exam].append({
            'activity': exam_name,
            'start_time': exam_start.time(),
            'end_time': exam_end,
            'color': "#534666"
        })

    # Determine the last exam date
    last_exam_date = max(exam.date() for exam in exams.values())
    today_date = datetime.today().date()
    days_until_last_exam = (last_exam_date - today_date).days

    # Add all events to the schedule
    for event_name, (event_start, duration) in events.items():

        event_end = (datetime.combine(datetime.today(), event_start) + timedelta(hours=duration)).time()
        

        days_with_events = [datetime.today().date() + timedelta(days=i) for i in range(days_until_last_exam)]
        for event_day in days_with_events:
            if event_day not in schedule:
                schedule[event_day] = []
            schedule[event_day].append({
                'activity': event_name,
                'start_time': event_start,
                'end_time': event_end,
                'color': "#DC8665"
            })
    

    # Distribute study time
    day_index = 0
    daily_study_hours = 6


    for study_day in (datetime.today().date() + timedelta(days=i) for i in range((last_exam_date - datetime.today().date()).days + 1)):
        # Skip to the next exam in the cycle if the current one is past
        while day_index < num_exams and study_day >= exams[exam_cycle[day_index]].date():
            day_index += 1

        if day_index >= num_exams:  # If all exams are past, stop
            continue

        # Select the exam for this day
        current_exam = exam_cycle[day_index]
        
        # Ensure the schedule for the current day exists
        if study_day not in schedule:
            schedule[study_day] = []
        
        # Avoid conflicts with events
        available_times = calculate_available_slots(study_day, schedule)
        
        # Allocate study time in all available slots until daily study goal is met
        allocated_hours = 0
        for slot_start, slot_end in available_times:
            # Calculate available hours in the slot
            available_hours = (datetime.combine(datetime.today(), slot_end) - datetime.combine(datetime.today(), slot_start)).total_seconds() / 3600
            study_hours = min(daily_study_hours - allocated_hours, available_hours)

            if study_hours <= 0:
                continue  # Skip if no study time needed or available

            # Calculate study start and end times
            study_start = slot_start
            study_end = (datetime.combine(datetime.today(), study_start) + timedelta(hours=study_hours)).time()

            # Add study session to the schedule
            schedule[study_day].append({
                'activity': f'Study {current_exam}',
                'start_time': study_start,
                'end_time': study_end,
                'color': "#EEB462"
            })

            allocated_hours += study_hours

            # Stop if daily study goal is reached
            if allocated_hours >= daily_study_hours:
                break
    
    return schedule

def calculate_available_slots(date, schedule):
    """Helper function to determine available time slots on a given day."""
    day_start = time(8, 0)
    day_end = time(22, 0)
    buffer = timedelta(minutes=30)
    
    # Collect event times with buffer
    event_slots = [
        (
            (datetime.combine(datetime.today(), activity['start_time']) - buffer).time(),
            (datetime.combine(datetime.today(), activity['end_time']) + buffer).time()
        )
        for activity in schedule.get(date, [])
    ]
    event_slots.sort()  # Sort by start time
    
    # Find free slots
    free_slots = []
    current_start = day_start
    
    for event_start, event_end in event_slots:
        if current_start < event_start:
            free_slots.append((current_start, event_start))  # Free time before event
        current_start = max(current_start, event_end)
    
    if current_start < day_end:
        free_slots.append((current_start, day_end))  # Free time after last event
    
    return free_slots