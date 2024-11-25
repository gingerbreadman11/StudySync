# simple_calendar_example.py

import streamlit as st
from streamlit_calendar import calendar

def main():
    st.title("Simple Calendar Example")

    # Define some sample events
    calendar_events = [
        {
            "title": "Event 1",
            "start": "2023-07-03",
            "end": "2023-07-05",
            "allDay": True,
            "backgroundColor": "#FF6C6C",
            "borderColor": "#FF6C6C",
            "resourceId": "a"
        },
        {
            "title": "Event 2",
            "start": "2023-07-01",
            "end": "2023-07-10",
            "allDay": True,
            "backgroundColor": "#FFBD45",
            "borderColor": "#FFBD45",
            "resourceId": "b"
        },
        {
            "title": "Event 3",
            "start": "2023-07-20",
            "allDay": True,
            "backgroundColor": "#FF4B4B",
            "borderColor": "#FF4B4B",
            "resourceId": "c"
        },
        {
            "title": "Event 4",
            "start": "2023-07-23",
            "end": "2023-07-25",
            "allDay": True,
            "backgroundColor": "#FF6C6C",
            "borderColor": "#FF6C6C",
            "resourceId": "d"
        },
        {
            "title": "Event 5",
            "start": "2023-07-29",
            "end": "2023-07-30",
            "allDay": True,
            "backgroundColor": "#FFBD45",
            "borderColor": "#FFBD45",
            "resourceId": "e"
        },
        {
            "title": "Event 6",
            "start": "2023-07-28",
            "allDay": True,
            "backgroundColor": "#FF4B4B",
            "borderColor": "#FF4B4B",
            "resourceId": "f"
        },
        {
            "title": "Event 7",
            "start": "2023-07-01T08:30:00+02:00",
            "end": "2023-07-01T10:30:00+02:00",
            "allDay": False,
            "backgroundColor": "#FF4B4B",
            "borderColor": "#FF4B4B",
            "resourceId": "a"
        },
        {
            "title": "Event 8",
            "start": "2023-07-01T07:30:00+02:00",
            "end": "2023-07-01T10:30:00+02:00",
            "allDay": False,
            "backgroundColor": "#3D9DF3",
            "borderColor": "#3D9DF3",
            "resourceId": "b"
        },
        {
            "title": "Event 9",
            "start": "2023-07-02T10:40:00+02:00",
            "end": "2023-07-02T12:30:00+02:00",
            "allDay": False,
            "backgroundColor": "#3DD56D",
            "borderColor": "#3DD56D",
            "resourceId": "c"
        },
        {
            "title": "Event 10",
            "start": "2023-07-15T08:30:00+02:00",
            "end": "2023-07-15T10:30:00+02:00",
            "allDay": False,
            "backgroundColor": "#FF4B4B",
            "borderColor": "#FF4B4B",
            "resourceId": "d"
        },
        {
            "title": "Event 11",
            "start": "2023-07-15T07:30:00+02:00",
            "end": "2023-07-15T10:30:00+02:00",
            "allDay": False,
            "backgroundColor": "#3DD56D",
            "borderColor": "#3DD56D",
            "resourceId": "e"
        },
        {
            "title": "Event 12",
            "start": "2023-07-21T10:40:00+02:00",
            "end": "2023-07-21T12:30:00+02:00",
            "allDay": False,
            "backgroundColor": "#3D9DF3",
            "borderColor": "#3D9DF3",
            "resourceId": "f"
        },
        {
            "title": "Event 13",
            "start": "2023-07-17T08:30:00+02:00",
            "end": "2023-07-17T10:30:00+02:00",
            "allDay": False,
            "backgroundColor": "#FF4B4B",
            "borderColor": "#FF4B4B",
            "resourceId": "a"
        },
        {
            "title": "Event 14",
            "start": "2023-07-17T09:30:00+02:00",
            "end": "2023-07-17T11:30:00+02:00",
            "allDay": False,
            "backgroundColor": "#3D9DF3",
            "borderColor": "#3D9DF3",
            "resourceId": "b"
        },
        {
            "title": "Event 15",
            "start": "2023-07-17T10:30:00+02:00",
            "end": "2023-07-17T12:30:00+02:00",
            "allDay": False,
            "backgroundColor": "#3DD56D",
            "borderColor": "#3DD56D",
            "resourceId": "c"
        },
        {
            "title": "Event 16",
            "start": "2023-07-17T13:30:00+02:00",
            "end": "2023-07-17T14:30:00+02:00",
            "allDay": False,
            "backgroundColor": "#FF6C6C",
            "borderColor": "#FF6C6C",
            "resourceId": "d"
        },
        {
            "title": "Event 17",
            "start": "2023-07-17T15:30:00+02:00",
            "end": "2023-07-17T16:30:00+02:00",
            "allDay": False,
            "backgroundColor": "#FFBD45",
            "borderColor": "#FFBD45",
            "resourceId": "e"
        }
    ]

    # Define resources if needed (for resource views)
    calendar_resources = [
        {"id": "a", "title": "Resource A"},
        {"id": "b", "title": "Resource B"},
        {"id": "c", "title": "Resource C"},
        {"id": "d", "title": "Resource D"},
        {"id": "e", "title": "Resource E"},
        {"id": "f", "title": "Resource F"}
    ]

    # Set calendar options
    calendar_options = {
        "initialView": "dayGridMonth",
        "headerToolbar": {
            "left": "prev,next today",
            "center": "title",
            "right": "dayGridMonth,timeGridWeek,timeGridDay"
        },
        "resources": calendar_resources,
        "navLinks": True,
        "editable": False,
        "selectable": True,
        "nowIndicator": True,
        "weekNumbers": False,
        "dayMaxEvents": True,
    }

    # Display the calendar
    calendar_value = calendar(
        events=calendar_events,
        options=calendar_options,
        custom_css='',
        callbacks=[]
    )

    st.write(calendar_value)

if __name__ == "__main__":
    main()
