import datetime
from datetime import timedelta

#this is the Miminal Viable Product (MVP) for the study plan generator
#to use it run "  python3 MVP.py   " in the terminal

def get_exam_info():
    exams = []
    num_exams = int(input("Enter the number of exams: "))
    for i in range(num_exams):
        print(f"\nExam {i+1}:")
        name = input("Enter exam name: ")
        
        # Get and validate exam date
        while True:
            date_str = input("Enter exam date (YYYY-MM-DD): ")
            try:
                exam_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                if exam_date < datetime.date.today():
                    print("Exam date cannot be in the past. Please enter a future date.")
                else:
                    break
            except ValueError:
                print("Invalid date format. Please enter in YYYY-MM-DD format.")
        
        # Get and validate difficulty level
        difficulty_levels = ['Easy', 'Medium', 'Hard']
        while True:
            difficulty = input("Enter difficulty level (Easy/Medium/Hard): ").capitalize()
            if difficulty in difficulty_levels:
                break
            else:
                print("Invalid difficulty level. Please choose from Easy, Medium, or Hard.")
        
        # Get and validate preparation time
        while True:
            try:
                prep_time = int(input("Enter desired preparation time in days: "))
                if prep_time <= 0:
                    print("Preparation time must be a positive integer.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        exam = {
            'name': name,
            'date': exam_date,
            'difficulty': difficulty,
            'prep_time': prep_time
        }
        exams.append(exam)
    return exams

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

def display_study_plan(study_plan):
    print("\nYour Study Plan:")
    for plan in study_plan:
        print(f"\nExam: {plan['exam_name']}")
        print("Study Sessions:")
        for session in plan['study_sessions']:
            print(f" - {session.strftime('%Y-%m-%d')}")

def main():
    exams = get_exam_info()
    study_plan = generate_study_plan(exams)
    display_study_plan(study_plan)

if __name__ == "__main__":
    main()
