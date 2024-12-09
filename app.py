import streamlit as st
import csv
from io import StringIO
from datetime import datetime
import ics
from gui_input import get_user_inputs
from calculations import generate_study_plan
from output_display import display_schedule
from conversion_to_calendar import generate_ics_from_csv

# Function to generate CSV data in memory
def generate_csv(schedule):
    output = StringIO()
    writer = csv.writer(output, delimiter=';')

    # Write header row
    writer.writerow(["Date", "Activity", "Start Time", "End Time", "Color"])

    # Write data rows
    for sched_date, activities in schedule.items():
        for activity in activities:
            writer.writerow([sched_date, activity['activity'], activity['start_time'], activity['end_time'], activity['color']])

    output.seek(0)
    return output.getvalue().encode('utf-8')  # Ensure UTF-8 encoding

def main():
    inputs = get_user_inputs()

    if st.session_state.get('plan_generated', False):
        schedule = generate_study_plan(inputs)
        display_schedule(schedule)

        # Generate and download CSV
        if st.button("Save Study Plan to CSV"):
            csv_data = generate_csv(schedule)
            st.download_button(
                label="Download Study Plan as CSV",
                data=csv_data,
                file_name="study_schedule.csv",
                mime="text/csv"
            )

        # Generate and download ICS directly
        if st.button("Save Study Plan to ICS"):
            csv_data = generate_csv(schedule).decode('utf-8')  # Decode to string for ICS conversion
            ics_data = generate_ics_from_csv(csv_data)

            if ics_data:
                st.success("ICS file generated successfully!")
                st.download_button(
                    label="Download Study Plan as ICS",
                    data=ics_data.encode('utf-8'),  # Convert to bytes for download
                    file_name="study_schedule.ics",
                    mime="text/calendar"
                )
            else:
                st.error("Failed to generate ICS file. Please check the log for errors.")

        # Download ICS (Test) - directly from memory
        # if st.button("Download ICS (Test)"):
        #     csv_data = generate_csv(schedule).decode('utf-8')  # Decode to string for ICS conversion
        #     ics_data = generate_ics_from_csv(csv_data)

        #     if ics_data:
        #         st.download_button(
        #             label="Download Study Plan as ICS (Test)",
        #             data=ics_data.encode('utf-8'),  # Convert to bytes for download
        #             file_name="study_schedule_test.ics",
        #             mime="text/calendar"
        #         )
        #     else:
        #         st.error("Failed to generate ICS file. Please check the log for errors.")

    else:
        st.write("Please enter your inputs and click 'Generate Study Plan'.")


if __name__ == '__main__':
    main()