# calculations.py

from datetime import datetime, timedelta, time

def generate_study_plan(inputs):
    study_plans = []
    study_schedule = {}  # Holds the overall schedule

    exams = inputs["exams"]
    sleep_start_time = inputs["sleep_start_time"]
    sleep_duration = inputs["sleep_duration"]
    eating_times = inputs["eating_times"]
    workout_times = inputs["workout_times"]

    today = datetime.today().date()
    end_date = max(exam["exam_date"] for exam in exams)

    total_days = (end_date - today).days + 1

    # Initialize study_schedule with empty days
    for i in range(total_days):
        date = today + timedelta(days=i)
        study_schedule[date] = []

    # Build fixed activities schedule for each day
    fixed_schedule = {}

    for i in range(total_days):
        date = today + timedelta(days=i)
        fixed_schedule[date] = []

        # Sleep times
        sleep_start_datetime = datetime.combine(date, sleep_start_time)
        sleep_end_datetime = sleep_start_datetime + timedelta(hours=sleep_duration)
        sleep_end_date = sleep_end_datetime.date()
        sleep_end_time = sleep_end_datetime.time()

        if sleep_end_date > date:
            # Sleep crosses midnight
            # Current day sleep
            fixed_schedule[date].append({
                "activity": "Sleep",
                "start_time": sleep_start_time,
                "end_time": time(23, 59, 59)
            })
            # Next day sleep
            next_day = date + timedelta(days=1)
            if next_day <= end_date:
                if next_day not in fixed_schedule:
                    fixed_schedule[next_day] = []
                fixed_schedule[next_day].append({
                    "activity": "Sleep",
                    "start_time": time(0, 0),
                    "end_time": sleep_end_time
                })
        else:
            # Sleep within the same day
            fixed_schedule[date].append({
                "activity": "Sleep",
                "start_time": sleep_start_time,
                "end_time": sleep_end_time
            })

        # Eating times
        for eating_time in eating_times:
            add_activity_to_schedule(fixed_schedule, date, end_date, "Eating", eating_time)

        # Workout times
        for workout_time in workout_times:
            add_activity_to_schedule(fixed_schedule, date, end_date, "Workout", workout_time)

    # For each exam, calculate study times and allocate into available slots
    for idx, exam in enumerate(exams):
        exam_name = exam["exam_name"]
        exam_date = exam["exam_date"]
        difficulty_level = exam["difficulty_level"]
        prep_time = exam["prep_time"]
        personal_preferences = exam["personal_preferences"]

        days_remaining = (exam_date - today).days + 1

        if days_remaining <= 0:
            study_plans.append({
                "exam_name": exam_name,
                "error": f"The exam date for '{exam_name}' must be in the future."
            })
            continue

        # Difficulty multipliers
        difficulty_multiplier = {
            "Easy": 0.8,
            "Medium": 1.0,
            "Hard": 1.2
        }

        # Calculate total adjusted preparation time
        adjusted_prep_time = prep_time * difficulty_multiplier[difficulty_level]

        # Distribute study time evenly across the days remaining
        daily_study_time = adjusted_prep_time / days_remaining

        # For each day, allocate study time into available slots
        for i in range(days_remaining):
            date = today + timedelta(days=i)
            if date > exam_date:
                continue

            # Get fixed activities for the day
            occupied_intervals = fixed_schedule.get(date, [])

            # Create a list of available intervals
            available_intervals = get_available_intervals(occupied_intervals)

            # Allocate study time into available intervals
            remaining_study_time = daily_study_time
            for interval in available_intervals:
                interval_start = interval["start_time"]
                interval_end = interval["end_time"]
                interval_duration = time_diff_in_hours(interval_start, interval_end)

                if interval_duration <= 0:
                    continue

                study_time = min(remaining_study_time, interval_duration)

                study_start_time = interval_start
                study_end_time = add_hours_to_time(study_start_time, study_time)

                # Handle crossing midnight for study times
                if time_compare(study_end_time, study_start_time) <= 0:
                    # Study time crosses midnight
                    # Add study block up to midnight
                    study_block_1 = {
                        "activity": "Study",
                        "exam_name": exam_name,
                        "start_time": study_start_time,
                        "end_time": time(23, 59, 59)
                    }
                    fixed_schedule[date].append(study_block_1)

                    # Add study block for the next day
                    next_day = date + timedelta(days=1)
                    if next_day <= end_date:
                        if next_day not in fixed_schedule:
                            fixed_schedule[next_day] = []
                        study_block_2 = {
                            "activity": "Study",
                            "exam_name": exam_name,
                            "start_time": time(0, 0),
                            "end_time": study_end_time
                        }
                        fixed_schedule[next_day].append(study_block_2)
                        # Update occupied intervals for the next day
                        occupied_intervals_next_day = fixed_schedule[next_day]
                        occupied_intervals_next_day.append(study_block_2)
                else:
                    # Study time within the same day
                    study_block = {
                        "activity": "Study",
                        "exam_name": exam_name,
                        "start_time": study_start_time,
                        "end_time": study_end_time
                    }
                    fixed_schedule[date].append(study_block)

                remaining_study_time -= study_time

                # Update occupied intervals
                occupied_intervals.append({
                    "activity": "Study",
                    "start_time": study_start_time,
                    "end_time": study_end_time
                })

                if remaining_study_time <= 0:
                    break

            if remaining_study_time > 0:
                # Not enough time to schedule all study time
                study_plans.append({
                    "exam_name": exam_name,
                    "error": f"Not enough available time on {date} to schedule all study time for '{exam_name}'."
                })

    # Convert fixed_schedule to study_schedule for plotting
    for date, activities in fixed_schedule.items():
        # Sort activities by start_time
        activities_sorted = sorted(activities, key=lambda x: x["start_time"])
        study_schedule[date] = activities_sorted

    return study_plans, study_schedule

def add_activity_to_schedule(fixed_schedule, date, end_date, activity_name, activity_time):
    start_time = activity_time["start_time"]
    duration = activity_time["duration"]
    end_time_datetime = datetime.combine(date, start_time) + timedelta(hours=duration)
    end_date_activity = end_time_datetime.date()
    end_time = end_time_datetime.time()

    if end_date_activity > date:
        # Activity crosses midnight
        # Current day activity
        fixed_schedule[date].append({
            "activity": activity_name,
            "start_time": start_time,
            "end_time": time(23, 59, 59)
        })
        # Next day activity
        next_day = date + timedelta(days=1)
        if next_day <= end_date:
            if next_day not in fixed_schedule:
                fixed_schedule[next_day] = []
            fixed_schedule[next_day].append({
                "activity": activity_name,
                "start_time": time(0, 0),
                "end_time": end_time
            })
    else:
        # Activity within the same day
        fixed_schedule[date].append({
            "activity": activity_name,
            "start_time": start_time,
            "end_time": end_time
        })

def get_available_intervals(occupied_intervals):
    # Given a list of occupied intervals (activities), return a list of available intervals
    # Occupied intervals are dictionaries with 'start_time' and 'end_time'
    # We assume the day starts at 0:00 and ends at 24:00

    # First, sort the occupied intervals by start_time
    occupied_intervals = sorted(occupied_intervals, key=lambda x: x["start_time"])

    available_intervals = []
    day_start = time(0, 0)
    day_end = time(23, 59, 59)

    # Initialize previous end time to day start
    prev_end_time = day_start

    for interval in occupied_intervals:
        start_time = interval["start_time"]
        end_time = interval["end_time"]

        # If there is a gap between prev_end_time and start_time, it's an available interval
        if time_compare(start_time, prev_end_time) > 0:
            available_intervals.append({
                "start_time": prev_end_time,
                "end_time": start_time
            })

        # Update prev_end_time
        if time_compare(end_time, prev_end_time) > 0:
            prev_end_time = end_time

    # After the last occupied interval, if there's time left until day_end
    if time_compare(day_end, prev_end_time) > 0:
        available_intervals.append({
            "start_time": prev_end_time,
            "end_time": day_end
        })

    return available_intervals

def time_compare(t1, t2):
    # Compare two time objects
    # Returns positive if t1 > t2, zero if equal, negative if t1 < t2
    datetime1 = datetime.combine(datetime.today(), t1)
    datetime2 = datetime.combine(datetime.today(), t2)
    delta = datetime1 - datetime2
    return delta.total_seconds()

def time_diff_in_hours(t1, t2):
    datetime1 = datetime.combine(datetime.today(), t1)
    datetime2 = datetime.combine(datetime.today(), t2)
    delta = datetime2 - datetime1
    total_hours = delta.total_seconds() / 3600.0
    if total_hours < 0:
        total_hours += 24  # Handle crossing midnight
    return total_hours

def add_hours_to_time(t, hours):
    datetime_t = datetime.combine(datetime.today(), t)
    new_datetime = datetime_t + timedelta(hours=hours)
    return new_datetime.time()
