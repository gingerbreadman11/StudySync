# output_display.py

import streamlit as st
from streamlit_calendar import calendar
import datetime  # Import the datetime module

def display_study_plan(study_plans, study_schedule):
    # First, display any error messages
    for plan in study_plans:
        if "error" in plan:
            st.error(plan["error"])

    st.header("📅 Your Study Schedule")

    # Prepare data for the calendar
    calendar_events = []

    activity_colors = {
        'Study': '#0000FF',  # Blue
    }

    for date, activities in study_schedule.items():
        for activity in activities:
            if activity.get('activity') != 'Study':
                continue  # Skip non-study activities

            title = activity.get('activity', 'Unknown')
            exam = activity.get('exam_name', '')
            if exam:
                title += f" ({exam})"

            # Get start and end times
            start_time = activity.get('start_time')
            end_time = activity.get('end_time')

            # Ensure start_time and end_time are strings
            if isinstance(start_time, datetime.time):
                start_time = start_time.strftime('%H:%M')
            if isinstance(end_time, datetime.time):
                end_time = end_time.strftime('%H:%M')

            # Parse times
            try:
                start_time_obj = datetime.datetime.strptime(start_time, '%H:%M').time()
                end_time_obj = datetime.datetime.strptime(end_time, '%H:%M').time()
            except ValueError:
                st.warning(f"Invalid time format for event '{title}' on {date}. Skipping.")
                continue

            start_datetime = datetime.datetime.combine(date, start_time_obj)
            end_datetime = datetime.datetime.combine(date, end_time_obj)

            # Handle crossing midnight
            if end_datetime <= start_datetime:
                end_datetime += datetime.timedelta(days=1)

            event = {
                'title': title,
                'start': start_datetime.isoformat(),
                'end': end_datetime.isoformat(),
                'allDay': False,
                'backgroundColor': activity_colors.get('Study', '#0000FF'),
                'borderColor': activity_colors.get('Study', '#0000FF'),
            }

            calendar_events.append(event)

    if not calendar_events:
        st.info("No study events to display.")
        return

    # Set calendar options
    calendar_options = {
        'initialView': 'timeGridWeek',
        'headerToolbar': {
            'left': 'prev,next today',
            'center': 'title',
            'right': 'dayGridMonth,timeGridWeek,timeGridDay',
        },
        'allDaySlot': False,
        'themeSystem': 'standard',
    }

    # Display the calendar
    try:
        calendar_value = calendar(
            events=calendar_events,
            options=calendar_options,
            custom_css='',
            key='study_calendar'
        )
        st.write(calendar_value)
    except Exception as e:
        st.error(f"An error occurred while displaying the calendar: {e}")
        st.write("Calendar events data:")
        st.write(calendar_events)
