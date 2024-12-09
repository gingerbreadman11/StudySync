import csv
from datetime import datetime

def export_schedule_to_csv(schedule, filename="study_schedule.csv"):
    # Öffne die Datei im Schreibmodus mit Windows-1252 Kodierung
    with open(filename, mode='w', newline='', encoding='windows-1252') as file:
        writer = csv.writer(file, delimiter=';')  # Verwende Semikolon als Trennzeichen

        # Schreibe die Header-Zeile
        writer.writerow(["Date", "Activity", "Start Time", "End Time", "Color"])

        # Schreibe die Daten
        for sched_date, activities in schedule.items():
            for activity in activities:
                writer.writerow([sched_date, activity['activity'], activity['start_time'], activity['end_time'], activity['color']])

    print(f"Schedule exported to {filename}")



    # Exportiere den Zeitplan als CSV
    export_schedule_to_csv(schedule)