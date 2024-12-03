# output_display.py

import streamlit as st
from streamlit_calendar import calendar
from datetime import datetime

def display_schedule(schedule):
    st.header("🗓️ Your Study Schedule")

    if not schedule:
        st.write("No schedule to display.")
        return

    # Prepare events for the calendar
    events = []
    for sched_date, activities in schedule.items():
        for activity in activities:
            start_datetime = datetime.combine(sched_date, activity['start_time'])
            end_datetime = datetime.combine(sched_date, activity['end_time'])


            # Assign colors based on the activity type
            if activity['activity'] == "Type 1":
                event_color = "blue"
            elif activity['activity'] == "Study":
                event_color = "red"
            else:
                event_color = "green"

            # Create event dictionary
            event = {
                'title': activity['activity'],
                'start': start_datetime.strftime('%Y-%m-%dT%H:%M:%S'),
                'end': end_datetime.strftime('%Y-%m-%dT%H:%M:%S'),
                'color': event_color,  # Add color property
                
            }
            events.append(event)

    # Calendar options
    calendar_options = {
        "editable": "true",
        "selectable": "true",
        "initialView": "timeGridWeek",
        "headerToolbar": {
            "left": "prev,next today",
            "center": "title",
            "right": "timeGridDay,timeGridWeek,dayGridMonth",
        },
        "allDaySlot": False,
        "slotMinTime": "00:00:00",
        "slotMaxTime": "24:00:00",
    }

    # Display the calendar
    calendar(events=events, options=calendar_options)
