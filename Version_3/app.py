import streamlit as st
import csv
from io import StringIO
from gui_input import get_user_inputs
from calculations import generate_study_plan
from output_display import display_schedule

# Funktion zum Erstellen der CSV-Datei im Speicher
def generate_csv(schedule):
    # Benutze StringIO, um die CSV-Datei im Speicher zu erstellen
    output = StringIO()
    writer = csv.writer(output, delimiter=';')

    # Schreibe die Header-Zeile
    writer.writerow(["Date", "Activity", "Start Time", "End Time", "Color"])

    # Schreibe die Daten
    for sched_date, activities in schedule.items():
        for activity in activities:
            writer.writerow([sched_date, activity['activity'], activity['start_time'], activity['end_time'], activity['color']])

    # Setze den Cursor an den Anfang der Datei, damit sie korrekt angezeigt wird
    output.seek(0)
    return output.getvalue()

def main():
    inputs = get_user_inputs()

    if st.session_state.get('plan_generated', False):
        # Generiere den Zeitplan
        schedule = generate_study_plan(inputs)
        display_schedule(schedule)
        
        # Button zum Erstellen und Anzeigen der CSV-Datei
        if st.button("Save Study Plan to CSV"):
            # Generiere die CSV-Daten
            csv_data = generate_csv(schedule)

            # Zeige die CSV-Daten in der App an
            st.text_area("Generated CSV:", csv_data, height=300)

            # Button zum Download der CSV-Datei
            st.download_button(
                label="Download Study Plan as CSV",
                data=csv_data,
                file_name="study_schedule.csv",
                mime="text/csv"
            )
    else:
        st.write("Please enter your inputs and click 'Generate Study Plan'.")

if __name__ == '__main__':
    main()