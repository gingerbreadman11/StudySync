# output_display.py

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def display_study_plan(study_plans, study_schedule):
    # First, display any error messages
    for plan in study_plans:
        if "error" in plan:
            st.error(plan["error"])

    st.header("📅 Your Weekly Schedule")

    # Prepare data for plotting
    schedule_data = []

    for date, activities in study_schedule.items():
        for activity in activities:
            entry = {
                'Date': date,
                'Activity': activity.get('activity', 'Unknown'),
                'Start': activity['start_time'],
                'End': activity['end_time'],
                'Exam': activity.get('exam_name', '')
            }
            schedule_data.append(entry)

    if not schedule_data:
        st.info("No schedule to display.")
        return

    # Convert to DataFrame
    df = pd.DataFrame(schedule_data)

    # Assign colors to activities
    activity_colors = {
        'Sleep': 'tab:gray',
        'Eating': 'tab:orange',
        'Workout': 'tab:green',
        'Study': 'tab:blue'
    }

    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 8))

    # Create a list of dates for the x-axis labels
    dates = sorted(df['Date'].unique())

    # Set up the y-axis for 24 hours
    ax.set_ylim(0, 24)

    # Map dates to x positions
    date_to_x = {date: idx for idx, date in enumerate(dates)}
    x_labels = [date.strftime('%Y-%m-%d') for date in dates]
    x_positions = list(range(len(dates)))

    # Plot the activities
    for idx, row in df.iterrows():
        x = date_to_x[row['Date']]
        y_start = row['Start'].hour + row['Start'].minute / 60.0
        y_end = row['End'].hour + row['End'].minute / 60.0
        duration = y_end - y_start
        if duration <= 0:
            duration += 24  # Handle crossing midnight

        ax.broken_barh(
            [(x - 0.4, 0.8)],  # x position and bar width
            (y_start, duration),  # y position and height
            facecolors=activity_colors.get(row['Activity'], 'tab:blue'),
            edgecolors='black'
        )

        # Annotate the activity
        label = row['Activity']
        if row['Activity'] == 'Study' and row['Exam']:
            label += f" ({row['Exam']})"

        ax.text(
            x,
            y_start + duration / 2,
            label,
            va='center',
            ha='center',
            color='white',
            fontsize=8,
            rotation=90
        )

    # Set the x-axis labels
    ax.set_xticks(x_positions)
    ax.set_xticklabels(x_labels, rotation=45, ha='right')

    # Set the y-axis labels
    ax.set_ylabel('Hour of Day')
    ax.set_yticks(range(0, 25, 2))
    ax.set_yticklabels([f"{i}:00" for i in range(0, 25, 2)])

    ax.set_xlabel('Date')
    ax.set_title('Weekly Schedule')
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Create a legend
    handles = [plt.Rectangle((0,0),1,1, color=color) for activity, color in activity_colors.items()]
    labels = activity_colors.keys()
    ax.legend(handles, labels, title='Activities', bbox_to_anchor=(1.05, 1), loc='upper left')

    st.pyplot(fig)
