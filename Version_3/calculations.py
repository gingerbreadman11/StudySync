from datetime import datetime, timedelta, time

def calculations(inputs):
    events, exams = inputs
    
    # Step 1: Initialize the schedule
    schedule = {}
    
    # Step 2: Add all events to the schedule
    for event_name, (event_start, duration) in events.items():
        # Calculate event end time
        event_end = (datetime.combine(datetime.today(), event_start) + timedelta(hours=duration)).time()
        
        # Add this event to all relevant days
        days_with_events = [datetime.today().date() + timedelta(days=i) for i in range(7)]  # Example: Add for a week
        for event_day in days_with_events:
            if event_day not in schedule:
                schedule[event_day] = []
            schedule[event_day].append({
                'activity': event_name,
                'start_time': event_start,
                'end_time': event_end,
            })
    
    # Step 3: Prepare a list of exams sorted by their dates
    sorted_exams = sorted(exams.items(), key=lambda x: x[1])  # Sort by exam date
    exam_cycle = [exam for exam, _ in sorted_exams]  # Maintain the cycle order
    num_exams = len(exam_cycle)
    
    # Step 4: Distribute study time across all exams
    day_index = 0
    for study_day in (datetime.today().date() + timedelta(days=i) for i in range(7)):
        if day_index >= num_exams:
            day_index = 0  # Cycle back to the first exam
        
        # Select the exam for this day
        current_exam = exam_cycle[day_index]
        exam_datetime = exams[current_exam]
        exam_date = exam_datetime.date()
        
        # Skip past exams
        if study_day >= exam_date:
            continue
        
        # Ensure the schedule for the current day exists
        if study_day not in schedule:
            schedule[study_day] = []
        
        # Avoid conflicts with events
        available_times = calculate_available_slots(study_day, schedule)
        
        # Allocate study time
        daily_study_hours = 2  # Example: 2 hours per day
        for slot_start, slot_end in available_times:
            study_start = slot_start
            study_end = (datetime.combine(datetime.today(), study_start) + timedelta(hours=daily_study_hours)).time()
            
            if study_end > slot_end:
                continue  # Not enough time in this slot
            
            # Add study session to the schedule
            schedule[study_day].append({
                'activity': f'Study {current_exam}',
                'start_time': study_start,
                'end_time': study_end,
            })
            break  # Move to the next day once study time is allocated
        
        # Move to the next exam in the cycle
        day_index += 1
    
    return schedule

def calculate_available_slots(date, schedule):
    """Helper function to determine available time slots on a given day."""
    day_start = time(8, 0)  # Example: Day starts at 08:00
    day_end = time(22, 0)   # Example: Day ends at 22:00
    
    # Collect event times
    event_slots = [
        (activity['start_time'], activity['end_time'])
        for activity in schedule.get(date, [])
    ]
    event_slots.sort()  # Sort by start time
    
    # Find free slots
    free_slots = []
    current_start = day_start
    
    for event_start, event_end in event_slots:
        if current_start < event_start:
            free_slots.append((current_start, event_start))
        current_start = max(current_start, event_end)
    
    if current_start < day_end:
        free_slots.append((current_start, day_end))
    
    return free_slots
