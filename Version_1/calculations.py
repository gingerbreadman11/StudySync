from datetime import datetime, timedelta

def generate_study_plan(inputs):
    exam_date = inputs["exam_date"]
    difficulty_level = inputs["difficulty_level"]
    prep_time = inputs["prep_time"]
    personal_preferences = inputs["personal_preferences"]

    today = datetime.today().date()
    days_remaining = (exam_date - today).days

    if days_remaining <= 0:
        return {"error": "The exam date must be in the future."}

    # Difficulty multipliers
    difficulty_multiplier = {
        "Easy": 0.8,
        "Medium": 1.0,
        "Hard": 1.2
    }

    # Calculate daily study time
    adjusted_prep_time = prep_time * difficulty_multiplier[difficulty_level]
    daily_study_time = adjusted_prep_time / days_remaining

    study_plan = {
        "days_remaining": days_remaining,
        "daily_study_time": round(daily_study_time, 2),
        "total_prep_time": prep_time,
        "difficulty_level": difficulty_level,
        "personal_preferences": personal_preferences
    }

    return study_plan
