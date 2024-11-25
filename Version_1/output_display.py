# output_display.py

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import itertools

def display_study_plan(study_plans, study_schedule):
    # First, display any error messages
    for plan in study_plans:
        if "error" in plan:
            st.error(plan["error"])

    st.header("📅 Your Weekly Study Schedule")

    # Prepare data for plotting
    schedule_data = []

    for date, blocks in study_schedule.items():
        for block in blocks:
            schedule_data.append({
                'Date': date,
                'Exam': block['exam_name'],
                'Start': block['start_hour'],
                'End': block['end_hour']
            })

    if not schedule_data:
        st.info("No study schedule to display.")
        return

    # Convert to DataFrame
    df = pd.DataFrame(schedule_data)

    # Assign colors to exams
    colors = itertools.cycle(['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown'])
    exam_colors = {}
    for exam in df['Exam'].unique():
        exam_colors[exam] = next(colors)

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create a list of dates for the x-axis labels
    dates = sorted(df['Date'].unique())

    # Set up the y-axis for 24 hours
    ax.set_ylim(0, 24)

    # Map dates to x positions
    date_to_x = {date: idx for idx, date in enumerate(dates)}
    x_labels = [date.strftime('%Y-%m-%d') for date in dates]
    x_positions = list(range(len(dates)))

    # Plot the study blocks
    for idx, row in df.iterrows():
        x = date_to_x[row['Date']]
        y_start = row['Start']
        y_end = row['End']
        ax.broken_barh(
            [(x - 0.4, 0.8)],  # x position and bar width
            (y_start, y_end - y_start),  # y position and height
            facecolors=exam_colors[row['Exam']],
            edgecolors='black'
        )

        # Annotate the exam name
        ax.text(
            x,
            (y_start + y_end) / 2,
            row['Exam'],
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
    ax.set_title('Weekly Study Schedule')
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Create a legend
    handles = [plt.Rectangle((0,0),1,1, color=exam_colors[exam]) for exam in exam_colors]
    labels = exam_colors.keys()
    ax.legend(handles, labels, title='Exams', bbox_to_anchor=(1.05, 1), loc='upper left')

    st.pyplot(fig)
