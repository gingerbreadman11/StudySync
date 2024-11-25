# calculations.py

from datetime import datetime, timedelta
import json

def generate_study_plan(exams):
    study_plans = []
    study_schedule = {}  # This will hold the overall study schedule

    today = datetime.today().date()
    end_date = max(exam["exam_date"] for exam in exams)

    total_days = (end_date - today).days + 1

    # Initialize study_schedule with empty days
    for i in range(total_days):
        date = today + timedelta(days=i)
        study_schedule[date] = []

    for idx, exam in enumerate(exams):
        exam_name = exam["exam_name"]
        exam_date = exam["exam_date"]
        difficulty_level = exam["difficulty_level"]
        prep_time = exam["prep_time"]
        personal_preferences = exam["personal_preferences"]

        days_remaining = (exam_date - today).days

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

        # Parse personal preferences for preferred study start time
        preferred_start_time = 18  # Default start time
        if personal_preferences:
            try:
                # Assume personal_preferences contains a preferred start time like "Start Time: 17"
                if "Start Time:" in personal_preferences:
                    preferred_start_time = int(personal_preferences.split("Start Time:")[1].strip().split()[0])
            except:
                pass  # Keep default if parsing fails

        # Ensure preferred_start_time is within 0-24
        if not (0 <= preferred_start_time < 24):
            preferred_start_time = 18

        # Allocate study times for each day
        for i in range(days_remaining):
            date = today + timedelta(days=i)
            if date > exam_date:
                continue

            study_start = preferred_start_time
            study_end = study_start + daily_study_time

            # Ensure study_end does not exceed 24 hours
            if study_end > 24:
                study_end = 24

            # Round study_start and study_end to nearest integer for plotting
            study_block = {
                "exam_name": exam_name,
                "start_hour": int(study_start),
                "end_hour": int(study_end)
            }

            # Add the study block to the schedule
            study_schedule[date].append(study_block)

        study_plan = {
            "exam_name": exam_name,
            "exam_date": exam_date,
            "days_remaining": days_remaining,
            "daily_study_time": round(daily_study_time, 2),
            "total_prep_time": prep_time,
            "difficulty_level": difficulty_level,
            "personal_preferences": personal_preferences
        }

        study_plans.append(study_plan)

    return study_plans, study_schedule
